import unittest

from unitcode.testcase.my_unit import Myunit


class Test1(unittest.TestCase):
    # def setUp(self) -> None:   #推荐这个方法返回None
    #     print("在每个测试用例之前执行")
    #
    # def tearDown(self) -> None:
    #     print("在每个测试用例之后执行")
    #
    # @classmethod  #装饰器，表示类方法
    # def setUpClass(cls) -> None:
    #     print("在每个类之前执行，初始化日志")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("在每个类之后执行，销毁日志")

    # age = 10


    def test1(self):
        """测试 01"""
        print("test01_1")
        self.assertTrue(True)

    def test2(self):
        print("test01_2")
    #
    # @unittest.skipIf(age<11,reason="年龄小于11")#肯定忽略
    def test3(self):
        print("test01_3")

    # @unittest.skipUnless(age>11,reason="年龄大于11")#否定忽略
    def test4(self):
        print("test01_4")



if __name__ == '__main__':
    print("--------main--------")
    unittest.main()


