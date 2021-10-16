# SWS Canteen Parser

Python code to fetch menu from sws2.maxmanager.xyz.

## Documentation

### Initialize browser
Initialize a new selenium webdriver (chrome) object.
```python
browser = init_browser()
```

Alternative:
```python
chrome_service = webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=chrome_service)
```

### Get canteen locations
Get all available canteen locations with location id \
```python
locations = get_locations(browser)
```

### Get today's menu
Get a dictionary of today's menu with allergens \
```python
menu = get_today_menu(browser, 16, "en")
```
