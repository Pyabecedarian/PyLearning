"""
返回简单值


定义一个函数, 用户输入first_name, middle_name和last_name
返回用户的全名

有些用户没有middle_name, 因此可选择性传递该参数

"""


def get_formatted_name(first_name, last_name, middle_name=""):
    """返回整洁的姓名"""

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


# name = get_formatted_name('jimi', 'hendrix')
# print(name)


"""
返回字典


函数可返回任何类型的值, 包括列表, 字典等复杂的数据结构


定义一个函数, 接受姓名的组成部分, 并返回一个表示人的列表

"""


def build_person(first_name, last_name, age=''):
    """返回一个字典, 其中包含有关一个人的信息"""

    person = {'first': first_name,
              'last': last_name}

    if age:
        person['age'] = age

    return person


# commander = build_person('tom', 'cruise', 29)
# print(commander)
