# SWS Canteen Parser

Python code to fetch menu from sws2.maxmanager.xyz.

## Documentation

Put 'mensa.py' in same folder as your python script.

### Initialize browser
Initialize a new selenium webdriver (chrome) object.
```python
import mensa
browser = mensa.init_browser()
```

Alternative:
```python
chrome_service = webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=chrome_service)
```

### Get canteen locations
Get all available canteen locations with location id \
```python
mensa.get_locations(browser)
```

### Get today's menu
Get a dictionary of today's menu with allergens \
```python
mensa.get_today_menu(browser, 16, "en")
```
