"""
for 循环遍历列表前, 确定列表不是空列表很重要

将列表名用于if语句中时, 若列表至少包含一个元素则返回True,
否则返回False

list_name = []
if list_name:
    things listed here won't be executed

"""


requested_toppings = []

if requested_toppings:  # 列表为空, 该代码块不会执行
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
