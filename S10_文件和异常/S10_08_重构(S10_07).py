"""
S10_07 能正常运行, 但还可以进一步改进.

利用 重构, 将代码划分为一系列完成具体工作的函数.
(使代码更清晰, 更易于理解, 更容易扩展)


重构 S10_07:
1>.  将其读取用户名的代码移到一个函数中, get_stored_usrname(),
     该函数尝试读取文件, 并返回文件中的用户名. 若没有发现文件, 则返回None

2>.  将存储新用户的代码移到另一个函数中, get_new_usrname(),
     该函数要求新用户输入姓名, 并将其存储在文件中

3>.  最后将向用户打招呼, 使用函数 greet_user(),
     完成S10_07的目标.
"""

import json


def get_stored_usrname():
    """
    如果存储了用户, 就获取它
    没有则返回None

    :return: 用户名 usrname
    """

    f_name = 'usrname.json'

    try:
        with open(f_name) as f_obj:
            usrname = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return usrname


def get_new_usrname():
    """
    如果没有用户信息, 就将询问其名字

    :return: 用户名 usrname
    """

    usrname = input("What's your name? ")
    file_name = 'usrname.json'
    with open(file_name, 'w') as f_obj:
        json.dump(usrname, f_obj)
        print("We'll remember you when you come back, " +
              usrname + '.')

    return usrname


def greet_user():
    """问候用户, 并指出它的名字"""

    usrname = get_stored_usrname()

    if usrname:
        print("Your name is " + usrname)
        usr_check = input("enter 'yes' to confirm, "
                          "'no' to enter a new name.")
        if usr_check.lower() == 'yes':
            print("Welcome back, " + usrname)
        else:
            usrname = get_new_usrname()
    else:
        usrname = get_new_usrname()
        print("We'll remember you when you come back, " +
              usrname + '.')


# 调用函数, 向用户打招呼
greet_user()
