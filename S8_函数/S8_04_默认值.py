"""
给形参指定默认值, 函数调用时可以不给该形参传递数据.

若传递了实参, 则形参的值就是实参的值

带默认值的形参应在参数列表的末尾

def func_name(arg_1, arg_2=sth)

                    注: 给形参指定默认值时, 等号两边不要有空格
                        对于函数调用中的关键字实参, 也如此

"""


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""

    print("\nI have a " + animal_type.title())
    print("My " + animal_type.title() + "'s name is " +
          pet_name.title())


describe_pet('harry')

# 使用位置实参调用
describe_pet('tom', 'cat')

# 使用关键字实参调用
describe_pet(animal_type='mouse', pet_name='jerry')
