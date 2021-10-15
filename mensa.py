import json
import requests


def get_week_menu() -> dict:
    """ Returns week's menu as dictionary

    Returns:
        (dict): week's menu
    """

    # get json from page
    menu_url = "https://sws.maxmanager.xyz/extern/mensa_central.json"
    r = requests.get(menu_url, stream=True)

    menu_obj = json.loads(r.content)

    return menu_obj


if __name__ == "__main__":
    print(get_week_menu("central"))
