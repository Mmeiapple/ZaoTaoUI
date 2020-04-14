import os
import time
from selenium import webdriver

current=os.path.dirname(__file__)
webdriverpath=os.path.join(current,'../webdriver/chromedriver.exe')

class SetDriver:
    def __init__(self):
        self.drivre=webdriver.Chrome(executable_path=webdriverpath)

    def Enter(self):
        self.drivre.get('http://172.16.4.221')
        self.drivre.implicitly_wait(30)
        self.drivre.maximize_window()
        return self.drivre
    def Quit(self):
        time.sleep(5)
        self.drivre.quit()
if __name__=='__main__':
    setDriver=SetDriver()
    setDriver.Enter()
