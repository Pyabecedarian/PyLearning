# 模块 collections 中的  OrderedDict 类 可以创建字典并记录键-值对顺序

"""
使用 OrderedDict类,

创建字典, 记录调查者喜好的语言与调查顺序
"""

from random import randint
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + '.')


"""
练习:

骰子: 模块 random 包含以各种方式生成随机数的函数, 其中 randint() 返回一个
位于指定范围内的整数, 例如, x = randint(1, 6)返回一个 1 ~ 6内的整数

请创建一个Die类, 它包含一个名为 sides 的属性(默认值为 6).
编写一个名为 roll_die()的方法, 它打印位于 1和骰子面数之间的随机数.
创建一个6面的骰子, 再投掷10次.
创建一个10面的骰子和一个20面的骰子, 并将它们都投掷10次.
"""


class Die:
    """骰子"""

    def __init__(self, sides=6):
        self._sides = sides

    def roll_die(self):
        """投骰子
        返回随机数
        """

        return randint(1, self._sides)


my_die_6 = Die()
print("\nRolling a die with 6 sides:")

i = 0
while i < 10:
    num = my_die_6.roll_die()
    print("Side: " + str(num))
    i += 1

die_10 = Die(10)
die_20 = Die(20)


print("\nRolling a die with 10 sides:")
i = 0
while i < 10:
    num = die_10.roll_die()
    print("Side: " + str(num))
    i += 1


print("\nRolling a die with 20 sides:")
i = 0
while i < 10:
    num = die_20.roll_die()
    print("Side: " + str(num))
    i += 1
