# -*- coding:utf-8 -*-
import time
import unittest
import random
from selenium.webdriver.common.by import By
from common.set_driver import SetDriver
from common.uesr_login import userLogin

class NewUser(unittest.TestCase):

    def setUp(self):
        self.driver=SetDriver()
        self.driver=self.driver.Enter()
        self.number=random.randint(0,1000)
    def tearDown(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//span[@class="user-name"][text()="admin"]').click()
        self.driver.find_element(By.XPATH,'//a[@href="/zentao/user-logout.html"]').click()
        time.sleep(2)
        self.driver.quit()

    def test_newuser(self):
        '''测试新建用户'''
        a = userLogin(self.driver,'admin','Hm123456')
        a.Userlogin()
        self.driver.find_element_by_xpath('//a[text()="组织"]').click()
        #点击添加用户
        self.driver.find_element_by_css_selector('a.btn.btn-primary i.icon.icon-plus').click()
        #选择部门
        self.driver.find_element_by_css_selector \
            ('div.chosen-container.chosen-container-single.chosen-compact.chosen-'
             'highlight-selected.chosen-with-search a.chosen-single').click()
        self.driver.find_element_by_css_selector('#dept_chosen > div > ul > li:nth-child(2)').click()
        #输入用户姓名
        self.driver.find_element_by_id('account').send_keys('test' + str(self.number))
        #输入用户密码
        self.driver.find_element_by_css_selector('input#password1').send_keys('tbody.table3243')
        #确认密码
        self.driver.find_element_by_css_selector('input#password2').send_keys('tbody.table3243')
        #输入真实姓名
        self.driver.find_element_by_xpath('//input[@id="realname"]').send_keys('测试' + str(self.number))
        #选择职位
        self.driver.find_element_by_css_selector('select#role').find_element_by_css_selector('option[value="qa"]').click()
        #权限分组
        self.driver.find_element_by_css_selector('#group_chosen > a').click()
        self.driver.find_element_by_css_selector('#group_chosen div.chosen-drop.chosen-auto-max-width.chosen-no-wrap.in '
                                            'ul.chosen-results li:nth-child(1)').click()
        #输入邮箱
        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys('hemei' + str(self.number) + '@qq.com')
        #性别选择
        self.driver.find_element_by_css_selector('input#genderf').click()
        self.driver.find_element_by_css_selector('input#verifyPassword').send_keys('Hm123456')
        #保存
        time.sleep(2)
        element1=self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        self.driver.execute_script('arguments[0].scrollIntoView();',element1)
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        time.sleep(2)
if __name__=="__main__":
    unittest.main(verbosity=2)
