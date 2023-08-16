import time
import  unittest
from HTMLTestRunner import HTMLTestRunner

from unitcode.testcase.test_unit01 import Test1
from unitcode.testcase.test_unit02 import NumbersTest
from unitcode.testcase.test_unit03 import Test3

if __name__ == '__main__':
    # #加载多个测试用例方式
    suite = unittest.TestSuite()
    # suite = unittest.TestSuite()#创建一个套件
    # suite.addTest(Test3("test1"))  #把测试用例加载到测试套件
    # suite.addTest(Test1("test1"))
    # suite.addTest(NumbersTest("test_even"))
    #
    # testcase = [Test3("test1"),Test1("test1")] #定义一个列表
    # suite.addTests(testcase) #addTests可以执行一个列表套件
    # #执行时一定要指定套件
    # unittest.main(defaultTest="suite")    #指定套件

    #
    # suite = unittest.defaultTestLoader.discover("./testcase", pattern='test*.py') #获得默认的测试加载器
    # unittest.main(defaultTest="suite")  #指定套件,verbosity=2代表运行的详细信息


#测试报告生成
# if __name__ == '__main__':
    # suite = unittest.defaultTestLoader.discover("./testcase", pattern='test*.py')  #
    # runner = unittest.TextTestRunner() #跟unittest.main直接运行结果一样
    # runner.run(suite)

    # HTML报告运行
