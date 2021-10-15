import json
import requests
from datetime import datetime


def get_menu_obj(mensa: str) -> dict:
    """

    Args:
        mensa (object): mensa to check menu. Possible values: central

    Returns:
        (dict): menu json object
    """
    menu_url = "https://sws.maxmanager.xyz/extern/mensa_{}.json".format(mensa)
    r = requests.get(menu_url, stream=True)

    return json.loads(r.content)


def get_today_menu(mensa: str) -> list:
    """ Returns today's menu as dictionary

    Args:
        mensa (str): mensa to check menu. Possible values: central

    Returns:
        (list): today's menu
    """

    menu = get_menu_obj(mensa)

    return_menu = []

    today_dt = datetime.today().strftime("%Y-%m-%d")

    for meal in menu["Mensa {}".format(mensa.capitalize())][today_dt]:
        return_menu.append({"meal": meal["meal"],
                            "price": meal["price1"],
                            "category": meal["category"].split()[0]})

    return return_menu
