# 3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
# 3-2 问候语：继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
# 3-3 自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like
# to own a Honda motorcycle”。

# names = ["A","B","C","D"]
# print(names[0],names[1],names[2],names[-1])
# message = "hello"
# print(message+names[0],message+names[1].lower(),message+names[2],message+names[-1])
# commut = ["地铁","自行车","摩托车"]
# print("我每天上班坐"+commut[0])

# 下面的练习比第 2 章的练习要复杂些，但让你有机会以前面介绍过的各种方式使用列表。
# 3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），
# 你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
# members = ["A","B","C"]
# print("邀请"+members[0],members[1],members[-1]+"共进晚餐")
# 3-5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
#  以完成练习 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
#  修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
#  再次打印一系列消息，向名单中的每位嘉宾发出邀请。
# print(members[1]+"不能来参加晚餐")
# members[1] = "E"
# print("邀请"+members[0],members[1],members[-1]+"参加晚餐")
# 3-6 添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
#  以完成练习 3-4 或练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
#  使用 insert()将一位新嘉宾添加到名单开头。
# print("我找到了更大的餐桌")
# members.insert(0,"Y")
# members.append("J")
# members.append("L")
# print("邀请"+members[0],members[1],members[2],members[3],members[-2],members[-1]+"参加晚餐")
# 3-8 放眼世界：想出至少 5 个你渴望去旅游的地方。
#  将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
#  按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
# Travel = ["xian","guizhou","beijing","changsha","gaochun"]
# print(Travel)
#  使用 sorted()按字母顺序打印这个列表，同时不要修改它。
#  再次打印该列表，核实排列顺序未变。
# print(sorted(Travel))
#  使用 sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
#  再次打印该列表，核实排列顺序未变。
# print(sorted(Travel, reverse=True))
#  使用 reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
#  使用 reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序
# Travel.reverse()
# print(Travel)
# Travel.reverse()
# print(Travel)
#  使用 sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
#  使用 sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
# Travel.sort()
# print(Travel)
# Travel.sort(reverse=True)
# print(Travel)

# 4-1 比萨：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用 for循环将每种比萨的名称都打印出来。
#  修改这个 for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
#  在程序末尾添加一行代码，它不在 for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
# pizzas = ["Domino","PapaJohns","Pizzahut"]
# for pizza in pizzas:
#     print("I like "+pizza.title()+" pizza")
# print("I really love pizza!\n")

# 4-2：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用 for 循环将每种动物的名称都打印出来。
#  修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
#  在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。

# animals = ["dog","cat","mouse"]
# for animal in animals:
#     print("A "+animal.title()+" would make a great pet")
# print("Any of these animals would make a great pet!")

# 4-3 数到 20：使用一个 for 循环打印数字 1~20（含）。
# numbers = []
# for number in range(1,21):
#     numbers.append(number)
# print(numbers)

# numbers = [ number for number in range(1,21) ]
# print(numbers)
# 4-4 一百万：创建一个列表，其中包含数字 1~1 000 000，再使用一个 for 循环将这些数字打印出来（如果输出的时间太长，按 Ctrl + C 停止输出，或关闭输出窗口）。
# numbers2 = [number for number in range(1,1000001)]
# print(numbers2)
# 4-5 计算 1~1 000 000 的总和：创建一个列表，其中包含数字 1~1 000 000，再使用min()和 max()核实该列表确实是从 1 开始，到 1 000 000 结束的。另外，对这个列表调
# 用函数 sum()，看看 Python 将一百万个数字相加需要多长时间。
# print(min(numbers2))
# print(max(numbers2))
# print(sum(numbers2))
# 4-6 奇数：通过给函数 range()指定第三个参数来创建一个列表，其中包含 1~20 的奇数；再使用一个 for 循环将这些数字都打印出来。
# jishu = []
# for number in range(1,20,2):
#     jishu.append(number)
# print(jishu)
# 4-7 3的倍数：创建一个列表，其中包含 3~30 内能被 3 整除的数字；再使用一个 for循环将这个列表中的数字都打印出来。
# _3beishu = [ ]
# for number in range (3,30):
#     if number%3 == 0:
#         _3beishu.append(number)
# print(_3beishu)
# 4-8 立方：将同一个数字乘三次称为立方。例如，在 Python 中，2 的立方用 2**3表示。
# 请创建一个列表，其中包含前 10 个整数（即 1~10）的立方，再使用一个 for 循环将这些立方数都打印出来。
# lifang = []
# for number in range(1,10):
#     number1 = number**3
#     lifang.append(number1)
# print(lifang)
# 4-9 立方解析：使用列表解析生成一个列表，其中包含前 10 个整数的立方。:
# lifang1 = [number**3 for number in range(1,11)]
# print(lifang1)

# 4-10 切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
#  打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
#  打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
#  打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
# print("The first three items in the list are:",lifang[:4])
# print("Three items from the middle of the list are:",lifang[3:6])
# print("The last three items in the list are:",lifang[-3:])

# 4-11 你的比萨和我的比萨：在你为完成练习 4-1 而编写的程序中，创建比萨列表的副本，并将其存储到变量 friend_pizzas 中，再完成如下任务。
#  在原来的比萨列表中添加一种比萨。
#  在列表 friend_pizzas 中添加另一种比萨。
#  核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一
# 个 for 循环来打印第一个列表；打印消息“My friend’s favorite pizzas are:”，再使
# 用一个 for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
# firend_pizzas = pizzas[:]
# pizzas.append("KFC")
# firend_pizzas.append("Mcdonalds")
#
# for pizza in pizzas:
#     print("My favorite pizzas are:",pizza)
#
# for pizza in firend_pizzas:
#     print("My friend’s favorite pizzas are:",pizza)

#
# 4-13 自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
#  使用一个 for 循环将该餐馆提供的五种食品都打印出来。
#  尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
#  餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个 for 循环将新元组的每个元素都打印出来。
#
# foods =("chai","mi","you","yan","shui")
# for food in foods:
#     print(food)

# foods[0] = "A"

# foods= ("A","B","C","D")
# for food in foods:
#     print(food)


# 6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键 first_name、last_name、age 和 city。将存储在该字典中的每项信息都打印出来。
# people = {}
# people['first_name']='A'
# people['last_name']='B'
# people['age']='16'
# people['city']='xian'
# print(people)

# 6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，
# 并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。
# numbers = {'A':'1',
#            'B':'2',
#            'C':'3',
#            'D':'4',
#            'E':'5'}
# print(numbers)

# 6-3 词汇表：Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
#  想出你在前面学过的 5 个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
#  以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；也可在一行打印词汇，
#再使用换行符（\n) 插入一个空行，然后在下一行以缩进的方式打印词汇的含义。

# glossary = {'list':'列表',
#             'tuple':'元组',
#             'dictionary':'字典',
#             'set':'集合',
#             'string':'字符串'}
#
# print('list:'+glossary['list'])
# print('tuple'+glossary['tuple'])
# print('dictionary:'+glossary['dictionary'])
# print('set'+glossary['set'])
# print('string:'+glossary['string'])

# 6-4 词汇表 2：既然你知道了如何遍历字典，现在请整理你为完成练习 6-3 而编写的代码，
# 将其中的一系列 print 语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，
# 再在词汇表中添加 5 个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
# glossary = {'list':'列表',
#             'tuple':'元组',
#             'dictionary':'字典',
#             'set':'集合',
#             'string':'字符串',
#             'int':'整数',
#             'float':'浮点',}
# for name,exp in glossary.items():
#     print(name+'意思是'+exp)
# print('\n')

# 6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt'。
#  使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
#  使用循环将该字典中每条河流的名字都打印出来。
#  使用循环将该字典包含的每个国家的名字都打印出来。
# Rivers = {'nile':'egypt',
#           'huanghe':'china',
#           'thames':'england'}
# for river,country in Rivers.items():
#     print('The '+river.title()+' runs through '+country.title())
# for river in Rivers.keys():
#     print(river.upper())
# for country in Rivers.values():
#     print(country.upper())
# print('\n')

# 6-6 调查：在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作。
#  创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
#  遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
# list = ['list','int','string','float']
# glossary2 = []
# for key in glossary:
#     glossary2.append(key)
# print(glossary2)
# for l in glossary2:
#     if l in list:
#         print(l.title()+' Thanks')
#     else:
#         print(l.title()+' invite')
# 6-7 人：在为完成练习 6-1 而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为 people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。/6-1使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
#  该字典应包含键 first_name、last_name、age 和 city。
people={'person1':{'first_name':'A',
                    'last_name':'A',
                    'age':'16',
                    'city':'Beijing'},
        'person2': {'first_name': 'B',
                    'last_name': 'B',
                    'age': '18',
                    'city': 'Nanjing'},
        'person3': {'first_name': 'C',
                    'last_name': 'C',
                    'age': '20',
                    'city': 'Dongjing'},
        }
for name,personinfo in people.items():
    fullname = personinfo['first_name']+personinfo['last_name']
    print("fullname is "+fullname)
    print('age is '+personinfo['age']+' live in '+personinfo['city'].title())

# 6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在
# 每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为 pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
dog = {'type':'dog',
       'master':'clive'}
cat = {'type':'cat',
       'master':'jier'}
mouse = {'type':'mouse',
         'master':'xide'}
pets=[dog,cat,mouse]
for pet in pets:
    print('type is '+pet['type']+', master is '+pet['master'])
# 6-9 喜欢的地方：创建一个名为 favorite_places 的字典。在这个字典中，将三个人的名字用作键；
# 对于其中的每个人，都存储他喜欢的 1~3 个地方。为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {'A':['beijing','nanjing','dongjing'],
                   'B':['hangzhou','shanghai'],
                   'C':['beihaidao']}
for name,place in favorite_places.items():
     if len(place) == 1:
        print(name+' favorite place is '+place[0])
     else:
        print(name+' has many favorite places are :')
        for p in place:
            print(p.title())
# 6-10 喜欢的数字：修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢
# 的数字，然后将每个人的名字及其喜欢的数字打印出来。
numbers = {'A':['1','10','100'],
           'B':['2','20'],
           'C':['3'],
           'D':['4'],
           'E':['5','50']}
for name,number in numbers.items():
    if len(number) == 1:
        print(name+" favorite number is "+number[0])
    else:
        print(name+" favorite number are:")
        for n in number:
            print(n)
# 6-11 城市：创建一个名为 cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，
# 并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含 country、population 和 fact 等键。将每座城市的名字以及有关它们的信息都打印出来。
cities = {'nanjing':{'country':'china',
                     'population':'900w',
                     'satuts':'capital'},
          'beijing':{'country':'china',
                     'population':'2000w',
                     'satuts':'capital'},
          'dongjing':{'country':'japan',
                     'population':'1500w',
                     'satuts':'capital'},
}
for city,cityinfo in cities.items():
    print(city+' is '+cityinfo['satuts']+' of '+cityinfo['country'].title())
    print("population of "+city+" is "+cityinfo['population'])