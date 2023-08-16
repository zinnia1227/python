


# while List1:
#     element = List1.pop()
#     print("移动元素为： "+element)
#     List2.append(element)
# print('\n打印新列表')
# for l in List2:
#     print("新列表元素为："+l)

# def printelement(a, b):
#     while a:
#         element = a.pop()
#         print("移动元素为： " + element)
#         b.append(element)
#
#
# def printnewlist(a):
#     for l in a:
#         print("新列表元素为：" + l)
#
#
# printelement(List1, List2)
# print('\n打印新列表')
# printnewlist(List2)
# def hello():
#     print("Hello, world!")
# # 计算面积的函数
# def area(width, height):
#     return width * height
#
# hello()
# width = 2
# height = 3
# print('width={}, height={}, area={}'.format(width, height, area(width, height)))

# def pet(animal,*name):
#     print('my '+ animal +'’s name are'+ str(name) )
#
#
# if __name__ == '__main__':
#     pet('dog', 'a', 'b', 'c')
#     pet('cat', 'dog', 'abc')

# def pet (**name):
#     print(name)
#
# pet1=pet(**{"name":"11","age":"18","dasda":"asds"})

# g_count = 0  # 全局作用域
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     # 闭包函数 inner()
#     def inner():
#         i_count = 2  # 局部作用域
# if 1:
#     sa = 2
# else:
#     sa = 3
# print('sa=', sa)
# print('o_count=', o_count)

# def res(x,y):
#     a=x-y
#     b=x+y
#     return a,b
# result = res(2,1)
# print(result[0],result[1])
# r1,r2 =res(2,1)
# print(r1,r2)

# def pet(name ,type):
#     print("My "+name+" is a "+type)
# if __name__ == '__main__':
#     pet('a', 'dog')

b=[1,2,3]
def change(a):
    global b
    a=[2,3,4]
change(b)
print(b)











