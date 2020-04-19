# --*utf-8*--
from selenium.webdriver.common.by import By

def login(driver,username,password):
    driver.find_element(By.XPATH, '//input[@placeholder="用户名"]').send_keys('qwe123')
    driver.find_element(By.XPATH, '//input[@placeholder="密码"]').send_keys('123456')
    driver.find_element(By.XPATH, '//div[text()="登录"]').click()
