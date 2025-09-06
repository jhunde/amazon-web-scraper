import csv
from bs4 import BeautifulSoup
from selenium import webdriver


# Start up driver
driver = webdriver.Chrome()


url = "https://www.amazon.com/"
driver.get(url)
