# 7-1 汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，
# 如“Let me see if I can find you a Subaru”。
# car = input("what car do you what  ")
# print("let me see if i can find you a " +car)

# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一 条消息，指出没有空桌；否则指出有空桌。
# peoplenumber = input('How many people came to dinner ')
# peoplenumber=int(peoplenumber)
#
# if peoplenumber >= 8:
#     print('sorry, There are no empty table here')
# else:
#     print('There have some empty tables here')

# 7-3 10 的整数倍：让用户输入一个数字，并指出这个数字是否是 10 的整数倍

number = input('enter a number ')
number = int(number)
if number % 10 == 0:
    print(str(number)+" is a multiole of 10")
else:
    print(str(number)+" is not a multiole of 10")