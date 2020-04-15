import os
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from common.set_driver import SetDriver
from common.uesr_login import userLogin
name=random.randint(0,1000)


class newProduct(unittest.TestCase):

    def setUp(self):
        self.driver=SetDriver()
        self.driver=self.driver.Enter()
    def tearDown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//span[@class="user-name"][text()="admin"]').click()
        self.driver.find_element(By.XPATH, '//a[@href="/zentao/user-logout.html"]').click()
        time.sleep(2)
        self.driver.quit()
    def test_newproduct(self):
        '''测试新建用户'''
        #登录
        a=userLogin(self.driver,'admin','Hm123456')
        a.Userlogin()
        time.sleep(2)
        # ----产品_新建产品----
        # 点击产品
        self.driver.find_element_by_link_text('产品').click()
        # 点击新建产品
        self.driver.find_element_by_xpath('/html/body/header/div[2]/div[1]/div[2]/div[1]/a[1]').click()
        # 输入产品名称
        self.driver.find_element_by_xpath('//input[@id="name"]').send_keys('CRM项目组02' + str(name))
        # 输入产品代号
        self.driver.find_element_by_css_selector('input#code').send_keys('00702' + str(name))
        # 选择测试负责人
        self.driver.find_element_by_css_selector('#QD_chosen').click()
        self.driver.find_element_by_css_selector('#QD_chosen > div > ul > li').click()
        # 选择发布负责人
        self.driver.find_element_by_css_selector('#RD_chosen > a').click()
        self.driver.find_element_by_css_selector('#RD_chosen > div > ul > li ').click()
        # 产品描述
        # 切进框架
        fpath = self.driver.find_element_by_xpath('//iframe[@class="ke-edit-iframe"]')
        self.driver.switch_to.frame(fpath)
        self.driver.find_element_by_css_selector('body.article-content').send_keys('测试何梅')
        # 切出框架
        self.driver.switch_to.default_content()
        # 保存表单
        self.driver.find_element_by_xpath('//button[text()="保存"]').submit()
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.title_contains('CRM项目组02')),'新建产品用例执行失败')

if __name__=="__main__":
    suite1=unittest.TestLoader().loadTestsFromTestCase(newProduct)
    # suite1=unittest.TestSuite(unittest.makeSuite(newProduct))
    unittest.main(defaultTest='suite1',verbosity=2)