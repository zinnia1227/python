import unittest

class Test3(unittest.TestCase):

    def test01(self):
        print("test1")
        # print(ord("1"))
        # print(ord("f"))
        # print(ord("e"))
        # print(ord("_"))
        # print(ord("0"))
        self.assertTrue(True)

#断言为错
    def testfalse(self):
        print("test2")
        self.assertTrue(False)

#抛出一个异常
    def testexception(self):
        print("test3")
        raise Exception("error")

#用例跳过
    @unittest.skip(reason="原因")
    def testskip(self):
        print("test4")

if __name__ == '__main__':
    print("--------main--------")
    unittest.main()




