import os
import time
import unittest
import HTMLTestRunner

nowtime=time.strftime('%Y-%m-%d-%H-%M-%S')
current=os.path.dirname(__file__)
test_casepath=os.path.join(current,'test_cases')
reporpath=os.path.join(current,'report/result%s.html'%nowtime)

discover=unittest.defaultTestLoader.discover(start_dir=test_casepath,
                                             pattern='*_case.py',
                                             top_level_dir=test_casepath)
allsuite=unittest.TestSuite()
allsuite.addTest(discover)


with open(reporpath,'wb') as file:
    allshuitereport=HTMLTestRunner.HTMLTestRunner(stream=file,
                                                  title='禅道自动化测试项目',
                                                  description='禅道UI用例执行')
    allshuitereport.run(allsuite)
