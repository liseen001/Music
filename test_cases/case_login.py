# --*utf-8*--
import time
from selenium import  webdriver
import unittest
from selenium.webdriver.common.by import By
from common import set_driver,login

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()

    def test_login(self):
        '''登录用例'''
        login.login(self.driver,'qwe123','123456')
        result =self.driver.title
        self.assertEqual(result,'test','登录失败')

    def tearDown(self):
        time.sleep(2)

if __name__=="__main":
    unittest.main(verbosity=2)