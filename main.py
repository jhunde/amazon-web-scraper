import csv
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Manually setting up ChromeDriver 
service = Service("C:/path/to/chromedriver.exe")

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(service=service, options=options)


# Start up driver
# driver = webdriver.Chrome()


url = "https://www.amazon.com"
driver.get(url)

def get_url(search_item):
    # generate url from seach term
    #   test a different approach here 
    template = "https://www.amazon.com/s?k={}&crid=2H2VCCND18SAD&sprefix=tv%2Caps%2C613&ref=nb_sb_noss_1"
    search_item = search_item.replace(' ', '+')  # using '+' char in the place of an empty space char 
    return template.format(search_item)

# test
url = get_url("tv remote")
print(url)