# --*utf-8*--
import time
import unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from common import set_driver

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()

    def test_login(self):
        self.driver.find_element(By.XPATH,'//input[@placeholder="用户名"]').send_keys('qwe123')
        self.driver.find_element(By.XPATH,'//input[@placeholder="密码"]').send_keys('123456')
        self.driver.find_element(By.XPATH,'//div[text()="登录"]').click()
        result =self.driver.find_element(By.XPATH,'//div[@class="footer-item"]').text
        self.assertEqual(result,'我的音乐','登录失败')

    def tearDown(self):
        time.sleep(2)

if __name__=="__main":
    unittest.main(verbosity=2)