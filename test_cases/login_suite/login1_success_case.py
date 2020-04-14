import os
import time
import random
import HTMLTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from common.set_driver import SetDriver
from common.uesr_login import userLogin


class ZaoTaologin01(unittest.TestCase):
    def setUp(self):
        self.driver=SetDriver()
        self.driver=self.driver.Enter()
    def tearDown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//span[@class="user-name"][text()="测试01"]').click()
        self.driver.find_element(By.XPATH, '//a[@href="/zentao/user-logout.html"]').click()
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        '''测试用户密码正确能否登陆'''
        a=userLogin(self.driver,'test1','A.123456')
        a.Userlogin()
        #断言，用户是否登陆成功
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="user-name"]'),'测试01'),'测试用户密码正确能否登陆执行失败')

if __name__=='__main__':
    nowtime = time.strftime('%Y-%m-%d-%H-%M-%S')
    current = os.path.dirname(__file__)
    webdriverpath = os.path.join(current, '../../webdriver/chromedriver.exe')
    reportpath = os.path.join(current, '../../report/result%s.html' % nowtime)
    suite1=unittest.TestLoader().loadTestsFromTestCase(ZaoTaologin01)
    with open(reportpath,'wb') as file:
        test_runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                                  title='登录模块',
                                                  description='密码正确登录成功测试用例')
        test_runner.run(suite1)