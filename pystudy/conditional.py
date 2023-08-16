# 5-3 外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green'、'yellow'或'red'。
#  编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了 5 个点。
#  编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
alien_color = 'green'
alien_color1 = 'yellow'
alien_color2 = 'red'
if alien_color == 'green':
    print("got 5 point\n")
if alien_color1 == 'green':
    print("got 5 point\n")

# 5-4 外星人颜色#2：像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个点。
#  如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 个点。
#  编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块。
if alien_color == 'green':
    print("got 5 point")
else:
    print("got 10 point")

if alien_color1 == 'greeen':
    print("got 5 point")
else:
    print("got 10 point\n")
# 5-5 外星人颜色#3：将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。
#  如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 个点。
#  如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 个点。
#  如果外星人是红色的，就打印一条消息，指出玩家获得了 15 个点。
#  编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
if alien_color == 'green':
    print("got 5 point")
if alien_color1 == 'yellow':
    print("got 10 point")
if alien_color2 == 'red':
    print("got 15 point\n")
# 5-6 人生的不同阶段：设置变量 age 的值，再编写一个 if-elif-else 结构，根据 age
# 的值判断处于人生的哪个阶段。
#  如果一个人的年龄小于 2 岁，就打印一条消息，指出他是婴儿。
#  如果一个人的年龄为 2（含）～4 岁，就打印一条消息，指出他正蹒跚学步。
#  如果一个人的年龄为 4（含）～13 岁，就打印一条消息，指出他是儿童。
#  如果一个人的年龄为 13（含）～20 岁，就打印一条消息，指出他是青少年。
#  如果一个人的年龄为 20（含）～65 岁，就打印一条消息，指出他是成年人。
#  如果一个人的年龄超过 65（含）岁，就打印一条消息，指出他是老年人。

age = 26
if age<2:
    print("婴儿")
elif age<4:
    print("蹒跚学步")
elif age<13:
    print("儿童")
elif age<20:
    print("青少年")
elif age<65:
    print("成年人\n")
else:
    print("老年人")

# 5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的 if语句，检查列表中是否包含特定的水果。
#  将该列表命名为 favorite_fruits，并在其中包含三种水果。
#  编写 5 条 if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，
# 就打印一条消息，如“You really like bananas!”。

favorite_fruits = ["apple","banana","peach"]
if "apple" in favorite_fruits:
    print("You really like apples")
if "banana" in favorite_fruits:
    print("You really like bananas")
if "peach" in favorite_fruits:
    print("You really like peaches")
if "A" in favorite_fruits:
    print("You really like A")
if "B" in favorite_fruits:
    print("You really like B")