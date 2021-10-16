import re
import json
from typing import List
import os
os.environ['WDM_LOG_LEVEL'] = '0'

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

url = r"https://sws2.maxmanager.xyz/"
roles = ('student', 'employee', 'other')
price_pattern = re.compile('\d+,\d\d')

ingredients = json.load(open("ingredients.json"))


def init_browser() -> object:
    """ Initialize new chrome browser

    Returns:
        (object): webdriver
    """
    chrome_service = webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=chrome_service)
    return browser


def get_locations(browser: object) -> dict:
    """ Return all available canteen locations with id and name

    Args:
        browser (object): selenium webdriver browser

    Returns:
        (list): locations, format: {id: name, id: name}
    """
    browser.get(url)

    # find select
    select_location = Select(browser.find_element(value="listbox-locations"))

    locations = {}
    for opt in select_location.options:
        locations[opt.get_attribute("value")] = opt.text

    return locations


def get_today_menu(browser: object, loc_id: int, lang: str = "en") -> List[dict]:
    """ Return today's menu of specified canteen

    Code based on https://github.com/cvzi/mensahd/blob/master/stuttgart/stuttgart_old_2020/__init__.py

    Args:
        browser (object): selenium webdriver browser
        loc_id (int): location id of canteen
        lang (str): Language [de, en]

    Returns:
        (List[dict]): list of dishes
    """

    if lang not in ["de", "en"]:
        lang = "en"

    browser.get(url + f"?lang={lang}")

    # change location to specified location id
    select_location = Select(browser.find_element(value="listbox-locations"))
    select_location.select_by_value(str(loc_id))

    # load html content to BeautifulSoup
    content = browser.page_source
    document = BeautifulSoup(content, "html.parser")

    divs = document.find(
        "div", {"class": "container-fluid"}).find_all("div", {"class", "row"})

    menu = []

    nextIsMenu = False
    categoryName = ""
    for div in divs:

        isCat = div.find("div", {"class": "gruppenname"})
        if isCat:
            categoryName = isCat.text.strip()
            categoryName = categoryName.replace("*", "").strip()
            categoryName = categoryName[0] + categoryName[1:].lower()

            nextIsMenu = False if categoryName in ("Hinweis", "Information") else True

            continue

        elif nextIsMenu:
            try:
                mealName = div.find("div", {"class": "visible-xs-block"}).text.strip()
            except AttributeError:
                continue

            if mealName.lower() == "geschlossen":
                nextIsMenu = False
                continue

            notes = div["lang"].split(",")

            # load allergens/ additives
            if len(notes):
                notes = [ingredients[lang][i] for i in notes if i in ingredients[lang]]
            else:
                notes = None

            menu.append({"category": categoryName, "meal": mealName, "ingredients": notes})

    return menu
