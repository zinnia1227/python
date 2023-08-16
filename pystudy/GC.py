import gc



class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(id(self)))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
#python默认是开启垃圾回收的，可以通过下面代码来将其关闭
gc.disable()
f2()

#

#
# class ClassA():
#     def __init__(self):
#         print('object born,id:%s'%str(id(self)))

#
# def f2():
#     while True:
#         c1 = ClassA()
#         c2 = ClassA()
#         c1.a = c2
#         c2.a = c1
#         del c1
#         del c2
#         gc.collect()
#
# f2()


# print(gc.get_threshold())
# print(gc.get_count())
# a = ClassA()
# print(gc.get_count())
# del a
# print(gc.get_count())