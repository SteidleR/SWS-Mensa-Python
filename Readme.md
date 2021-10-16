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

Example dictionary of locations
```python
{
  2: 'MENSA STUTTGART-VAIHINGEN',
  16: 'MENSA CENTRAL', 
  4: 'MENSA MUSIKHOCHSCHULE',
  7: 'MENSA KUNSTAKADEMIE', 
  1: 'MENSA LUDWIGSBURG', 
  6: 'MENSA FLANDERNSTRAßE', 
  9: 'MENSA ESSLINGEN STADTMITTE', 
  12: 'MENSA AM CAMPUS HORB', 
  13: 'MENSA GöPPINGEN', 
  21: 'FOODTRUCK'
}

```

### Get today's menu
Get a dictionary of today's menu with allergens \
```python
menu = get_today_menu(browser, 16, "en")
```

Example dictionary of menu
```python
[
  {
    'category': 'Main dish', 
    'meal': 'Vegetable sitr fry sweet sour', 
    'ingredients': []
  },
  {
    'category': 'Main dish', 
    'meal': 'Omelette with leaf spinach and salt potatoes', 
    'ingredients': ['egg', 'milk und lactose', 'wheat']
  }, 
  {
    'category': 'Side dish', 
    'meal': 'pumpkin carrots vegetable', 
    'ingredients': []
  }, 
  {
    'category': 'Dessert', 
    'meal': 'vanilla pudding', 
    'ingredients': ['milk und lactose']
  }
]
```
