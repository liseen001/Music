# --*utf-8*--
import os
from selenium import webdriver
def set_driver():
    current_path = os.path.dirname(__file__)
    foxfire_driver_path = os.path.join(current_path, '../webdriver/geckodriver')
    driver = webdriver.Firefox(executable_path=foxfire_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://172.20.10.13:8088/#/login')
    return driver