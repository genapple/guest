#-*- coding:UTF-8 -*-
import unittest
import unittest
from module1 import Calculator
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "C:/Users/shasha.yan/guest/guest/settings.py")
class ModuleTest(unittest.TestCase):
    def setUp(self):#用于测试用例执行前的初始化工作
        self.cal=Calculator(8,4)
    def tearDown(self):#用于测试用例执行后的善后工作
        pass
    def test_add(self):
        result=self.cal.add()
        self.assertEqual(result,12)
    def test_sub(self):
        result=self.cal.sub()
        self.assertEqual(result,4)
    def test_mul(self):
        result=self.cal.mul()
        self.assertEqual(result,32)
    def test_div(self):
        result=self.cal.div()
        self.assertEqual(result,2)
if __name__ == '__main__':
        #uniitest.main
        #构造测试集
        django.setup()
        suite=unittest.TestSuite()
        suite.addTest(ModuleTest("test_add"))
        suite.addTest(ModuleTest("test_sub"))
        suite.addTest(ModuleTest("test_mul"))
        suite.addTest(ModuleTest("test_div"))
        #执行测试
        # runner=unittest.TextTestRunner()
        runner=unittest.main()
        runner.run(suite)

