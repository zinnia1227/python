# # class test:
# #     def t1(self):
# #         print("1")
# #
# #     def t2(self):
# #         print("02")
# #
# # def main():
# #     t = test()
# #     test.t2()
# #
# # if __name__ == '__main__':
# #     main()
#
# class Test(object):
#
#     def t10(self):
#         print ('01')
#     @classmethod
#     def t20(cls):
#         print("02")
#
# def main():
#     test = Test()
#     test.t10()
#
#     # Test.t10()
#     Test.t20()
#
# if __name__ == '__main__':
#     main()
# import unittest
# class Testcase(unittest.TestCase):
#     def test(self,do_assert=False):
#         a= True
#         self.assertTrue(a,do_assert)
i = 0
num = 0
while i < 4:
    num = num+1
    i = i+1
    print(num)