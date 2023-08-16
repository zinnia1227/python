import  unittest

# from unitcode.testcase.Base import Base
from selenium import webdriver

from unitcode.testcase.Base import Base


class Myunit(unittest.TestCase):
    def setUp(self) -> None:   #推荐这个方法返回None
        print("在每个测试用例之前执行")

    def tearDown(self) -> None:
        print("在每个测试用例之后执行")

    @classmethod  #装饰器，表示类方法
    def setUpClass(cls) -> None:
        print("在每个类之前执行，初始化日志")

    @classmethod
    def tearDownClass(cls) -> None:
        print("在每个类之后执行，销毁日志")

# class Myunit(unittest.TestCase):
#     def setUp(self) :
#         self.b = Base()
#         self.driver = self.b.open_browser()
#         self.b.get("https://www.baidu.com/")
#
#
#     def tearDown(self) -> None:
#         print("在每个测试用例之后执行")
#
#     @classmethod  #装饰器，表示类方法
#     def setUpClass(cls) -> None:
#         print("在每个类之前执行，初始化日志")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("在每个类之后执行，销毁日志")