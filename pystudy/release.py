import sys
from datetime import datetime
import time
import os
import psutil

# def rename(a):
#     a = a+[6]
# b = [1,2,3]
# print(b)
# rename(b)
# print(b)




# a = 1
# b = a
# a = a+1




# a = 1
# print(id(a))
# print(type(a))
# print("改变a的指向")
# a = "1"
# print(id(a))
# print(type(a))


# def rename(a):
#     a = a + [4]
# b = [1,2,3]
# print(b)
# rename(b)
# print(b)





#作用域


# print(abs(-23))
# abs = 12
# print(abs(-23))


# a = 23
# def test():
#     a=12
#     print(a)
# test()


# list = [i for i in range(100) if i%2 == 0]
# print(list)
# print(i)
# a =1
# print(globals())
# a = 1
# def test():
#     a = 12
#     def test1():
#         # a =123
#         print(a)
#     test1()
#     print(a)
# test()
# print(a)


# a = 0
# def test():
#     a =0
#     def test1():
#         nonlocal a
#         a = 0
#         for i in range(10):
#             a += i
#     test1()
#     print(a)
# test()
# print(a)


# a = 0
# def test():
#     a = 2
#     def test1():
#         print(a)
#     test1()
# test()
# print(a)

# a = 0
# def test():
#     global a
#     a = 2
#     def test1():
#         a =0
#         def test2():
#             nonlocal a
#             a = 0
#             for i in range(10):
#                 a += i
#         test2()
#         print(a)
#     test1()
#     print(a)
# test()
# print(a)


# a = 1
# b = a
# print(id(a))
# print(id(b))

# class Pyobj():
#     def __del__(self):
#         print("del方法被调用，对象被销毁")
#
# print("开始")
# obj = Pyobj()
# obj = 6
# print("结束")


# a = [1]
# print(a)
# print(id(a))
# a.append(2)
# print(a)
# print(id(a))


# def add_pet(pet,pet_list=[]):
#     pet_list.append(pet)
#     print(pet_list)

# pet1 = ['dog','cat']
# add_pet('rabbit',pet1)

#


# print(add_pet.__defaults__)
# add_pet('dog')
# print(add_pet.__defaults__)
# add_pet('cat')
# print(add_pet.__defaults__)


# def add_pet(pet):
#     pet_list = []
#     pet_list.append(pet)
#     # print(pet_list)
# #
# #
# print(add_pet.__defaults__)  # (None,)
# add_pet('dog')
# print(add_pet.__defaults__)  # (None,)
# add_pet('cat')
# print(add_pet.__defaults__)  # (None,)


# def display_time(data=datetime.now()):
#     print(data.strftime('%B %d,%Y  %H:%M:%S'))
# display_time()


# def display_time():
#     data = datetime.now()
#     print(data.strftime('%B %d,%Y  %H:%M:%S'))
# print(display_time.__defaults__)
# display_time()
# time.sleep(2)
# display_time()
# time.sleep(2)
# display_time()
# time.sleep(2)

# def display_time(data=None):
#     if data == None:
#         data = datetime.now()
#         print(data.strftime('%B %d,%Y  %H:%M:%S'))
#
# display_time()
# time.sleep(2)
# display_time()
# time.sleep(2)
# display_time()
# time.sleep(2)



# a = 131321
# b = 131321
# c = -7
# print(id(a))
# print(id(b))
# print(id(c))






# 打印当前程序占用的内存大小
# def print_memory_info(name):
#     pid = os.getpid()
#     p = psutil.Process(pid)
#
#     info = p.memory_full_info()
#     MB = 1024 * 1024
#     memory = info.uss / MB
#     print('%s used %d MB' % (name, memory))


# 测试函数
# def foo():
#     print_memory_info("foo start")
#     length = 1000 * 1000
#     # global list
#     list = [i for i in range(length)]
#     print_memory_info("foo end")
#     return list

# def foo():
#     print_memory_info("foo start")
#     length = 1000 * 1000
#     list_a = [i for i in range(length)]
#     list_b = [i for i in range(length)]
#     list_a.append(list_b)
#     list_b.append(list_a)
#     print_memory_info("foo end")
#
#
# foo()
# print_memory_info("main end")



# class pet():
#     def __del__(self):
#         print("del方法被调用，对象被销毁")
#
# print("开始")
# p = pet()
# p = 1
# print("结束")

# a = 1
# print(globals())

# a = 6231
# a = 122

# def test():
#     global a
#     a = 2
#     def test1():
#         a =0
#         def test2():
#             nonlocal a
#             a = 0
#             for i in range(10):
#                 a += i
#         test2()
#         print(a)
#     test1()
#     print(a)
# test()
# print(a)
#



# 打印当前程序占用的内存大

# 打印当前程序占用的内存大小
def print_memory_info(name):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    MB = 1024 * 1024
    memory = info.uss / MB
    print('%s used %d MB' % (name, memory))


def foo():
    print_memory_info("foo start")
    length = 1000 * 1000
    list_a = [i for i in range(length)]
    list_b = [i for i in range(length)]
    list_a.append(list_b)
    list_b.append(list_a)
    print_memory_info("foo end")

foo()
print_memory_info("main end")