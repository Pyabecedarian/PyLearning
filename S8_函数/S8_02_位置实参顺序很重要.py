"""
位置实参

实参的传递方式有多种, 其中一种是位置实参

使用位置实参来调用函数时,如果实参的顺序应与函数内部形参的顺序保持一致

"""


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""

    print("\nI have a " + animal_type.title() + '.')
    print("My " + animal_type.title() + "'s name is " +
          pet_name.title())


describe_pet('hamster', 'harry')

# 调换实参位置将使结果变得出乎意料
# describe_pet('harry', 'hamster')
