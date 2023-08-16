
# message = "hello world"
# print(message)
#
# message = "hello python world"
# print(message)


# message = "so tried"
# print(message)
# print(message.title())
# print(message.upper())
# print(message.lower())
# print("\tso tried")

# message = "四大名著：\n\t红楼梦\n\t西游记\n\t三国演义\n\t水浒传 "
# print(message)

# 2-3 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示
# 的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。

# name = "eric"
# print("Hello "+name+", would you like to learn some Python today")

# 2-4 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母
# 大写的方式显示这个人名。
# print(name.title())
# print(name.upper())
# print(name.lower())

# 2-5 名言：找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
# print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

# 2-6 名言 2：重复练习 2-5，但将名人的姓名存储在变量 famous_person 中，再创建要显示的消息，并将其存储在变量 message 中，然后打印这条消息。
# famous_person = "Albert Einstein"
# message = '“A person who never made a mistake never tried anything new.”'
# print(famous_person+" once said, "+message)

# 2-7 剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数 lstrip()、rstrip()和 strip()对人名进行处理，并将结果打印出来。
# person = "\tdaiyu\n黛玉"
# print(person)
# print(person.lstrip()+"\n"+person.rstrip()+"\n"+person.strip())

#2-8 数字 8：编写 4 个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字 8。为使用 print 语句来显示结果
# print(5+3)
# print(10-2)
# print(4*2)
# print(int(8/1))

# 2-9 最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。
# number = 27
# print("my favorite number is "+str(number))