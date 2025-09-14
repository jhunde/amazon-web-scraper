import csv
from bs4 import BeautifulSoup
from selenium import webdriver
'''
# Firefox
driver = webdriver.Firefox()

# Google Chrome
driver = webdriver.Chrome()
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome example
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

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
# print(url)


# Extract collections 
soup = BeautifulSoup(driver.page_source, 'html.parser')         # retrieve html text
result = soup.find_all('div', {'data-component-type': "s-search-result"})
print(len(result))