"""
传递任意数量的实参

    定义: def func_name(*arg)

    调用: func_name(arg1, arg2, ...)

参数名 *arg 让Python创建一个名为 arg的空元组, 并将所有收到的值都封装在这个元组中.
即便函数只收到一个值也是如此.

"""


def make_pizza(size, *toppings):
    """
    打印顾客店的所有配料
    :param toppings: 配料
    """

    print("\nMaking a " + str(size) + "-inch pizza with the "
                                      "following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(12, 'mushroom', 'extra cheese', 'pepperoni')
make_pizza(6, 'extra cheese')


"""
任意数量的 关键字实参

需要接受任意数量的实参, 但预先不知道传递给函数会是什么信息. 这种情况下可将函数
编写成能够接受任意数量的 键-值 对

    定义: def func_name(arg1, arg2, ... , **arg)
    
两个星号让Python创建一个名为arg的空字典, 将收到的所有名称-值都封装到这个字典中

"""


def build_profile(first, last, **user_info):
    """创建一个字典, 其中包含我们知道的有关用户的一切"""

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics',
                             nation='USA')

print(user_profile)
