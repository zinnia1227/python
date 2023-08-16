# 9-1 餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type。创建一个名为 describe_restaurant()的方法和
# 一个名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print(self.restaurant_name.title()+" is a "+self.cuisine_type)
#     def open_restaurant(self):
#         print(self.restaurant_name.title()+" is open")
# restaurant = Restaurant("nanshanweng","chuancaiguan")
# print(restaurant.restaurant_name,restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 9-2 三家餐馆：根据你为完成练习 9-1 而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。
# restaurant2 = Restaurant("daimei","huoguo")
# restaurant2.describe_restaurant()
# restaurant3 = Restaurant("shengjiangshan","zizhu")
# restaurant3.describe_restaurant()
# 9-3 用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def describe_user(self):
#         print("用户名为："+self.first_name+" "+self.last_name)
#     def greet_user(self):
#         print("你好，"+self.first_name+" "+self.last_name)
# User1=User("zhang","san")
# User1.describe_user()
# User1.greet_user()
# User2=User("zhao","si")
# User2.describe_user()
# User2.greet_user()
# # 9-4 就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served的属性，并将其默认值设置为 0。
# # 根据这个类创建一个名为 restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# # 添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# # 添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。
# # 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def set_number_served(self,number):
#         self.number_served=number
#     def increment_number_served(self,add):
#         self.number_served += add
#     def print_number_served(self):
#         print("The number of people served in the restaurant is "+str(self.number_served))
#
# restaurant = Restaurant("nanshanweng","chuancaiguan")
# restaurant.number_served=3
# print(restaurant.number_served)
# restaurant.set_number_served(6)
# restaurant.print_number_served()
# restaurant.set_number_served(500)
# restaurant.increment_number_served(20)
# restaurant.print_number_served()
# 9-5 尝试登录次数：在为完成练习 9-3 而编写的 User 类中，
# 添加一个名为login_attempts 的属性。
# 编写一个名为 increment_login_attempts()的方法，它将属性login_attempts 的值加 1。
# 再编写一个名为 reset_login_attempts()的方法，它将属性login_attempts 的值重置为 0。
# 根据 User 类创建一个实例，再调用方法 increment_login_attempts()多次。
# 打印属性 login_attempts 的值，确认它被正确地递增；然后，调用方法 reset_login_attempts()，
# 并再次打印属性 login_attempts 的值，确认它被重置为 0。
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.login_attempts=0
#     def describe_user(self):
#         print("用户名为："+self.first_name+" "+self.last_name)
#     def greet_user(self):
#         print("你好，"+self.first_name+" "+self.last_name)
#     def return_name(self):
#         return self.first_name+" "+self.last_name
#     def increment_login_attempts(self):
#         self.login_attempts +=1
#     def reset_login_attempts(self):
#         self.login_attempts = 0
# User1=User("zhang","san")
# User1.increment_login_attempts()
# User1.increment_login_attempts()
# print("当前登录次数为"+str(User1.login_attempts))
# User1.reset_login_attempts()
# print("重置后登录次数为"+str(User1.login_attempts))

# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，
# 让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为 flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，并调用这个方法。
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors=["Pineapple","strawberry "]
#     def describe_icecream(self):
#         for i in self.flavors:
#             print(self.restaurant_name+" have "+i)
# Ice2 = IceCreamStand("strawberry shop","icecream")
# Ice2.describe_icecream()

# 9-7 管理员：管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承你为完成练习 9-3 或练习 9-5 而编写的 User 类。
# 添加一个名为 privileges 的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为 show_privileges()的方法，它显示管理员的权限。创建一个 Admin实例，并调用这个方法。

# 9-8 权限：编写一个名为 Privileges 的类，它只有一个属性——privileges，其中存储了练习 9-7 所说的字符串列表。
# 将方法 show_privileges()移到这个类中。在 Admin类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，
# 并使用方法show_privileges()来显示其权限

# class Privileges():
#     def __init__(self):
#         self.privileges=["can add post","can delete post","can ban user"]
#     def show_privileges(self):
#         for i in self.privileges:
#             print("权限:"+i)
# class Admin(User):
#     def __init__(self,first_name,last_name):
#         super().__init__(first_name,last_name)
#         self.privileges=Privileges()
#
# admin = Admin("zhang","san")
# admin.privileges.show_privileges()

class people():
    def __init__(self,name=1,age):
        self.name=name
        self.age =age
    def show(self):
        print(str(self.name)+str(self.age))

p = people(12,"1")

p.show()