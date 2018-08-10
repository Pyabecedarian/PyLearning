"""
函数

是带名字的代码块, 用于完成具体的工作
可被其他模块中import导入, 并使用它们

定义函数:

def func_name():
    ""'Docstring'""

    do sth...

    return sth


"""


# 定义函数/传递实参

def greet_user(username):
    """显示简单的问候语"""

    print("Hello " + username.title())


greet_user('sarah')
greet_user('chris')
