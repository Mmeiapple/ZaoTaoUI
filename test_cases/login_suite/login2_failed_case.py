import os
import time
import HTMLTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from common.set_driver import SetDriver
from common.uesr_login import userLogin

class ZaoTaologin02(unittest.TestCase):
    def setUp(self):
        self.driver = SetDriver()
        self.driver=self.driver.Enter()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        '''测试用户密码错误能否登陆'''
        a=userLogin(self.driver,'test1','123456')
        a.Userlogin()
        #断言，是否有弹窗并返会弹窗内容
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))

if __name__=='__main__':
    nowtime = time.strftime('%Y-%m-%d-%H-%M-%S')
    current = os.path.dirname(__file__)
    webdriverpath = os.path.join(current, '../../webdriver/chromedriver.exe')
    reportpath = os.path.join(current, '../../report/result%s.html' % nowtime)
    suite1=unittest.TestLoader().loadTestsFromTestCase(ZaoTaologin02)
    with open(reportpath,'wb') as file:
        test_runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                                  title='登录模块',
                                                  description='密码错误登录失败测试用例')
        test_runner.run(suite1)