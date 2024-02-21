from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_driver():
    options = webdriver.FirefoxOptions()    
    options.add_argument("--headless")
    driver = webdriver.Firefox(options = options)
    return driver
