import os
from selenium  import webdriver
from selenium.webdriver.common.by import By
from common.set_driver import SetDriver


class userLogin:
    def __init__(self,driver,username,password):
        self.driver=driver
        self.username=username
        self.password=password
    def Userlogin(self):
        self.driver.find_element(By.XPATH, '//a[@id="zentao"]').click()
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys(self.username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
if __name__=="__main__":
    driver01=SetDriver().Enter()
    driver02=userLogin(driver01,'test1','A.123456')
    driver02.Userlogin()

