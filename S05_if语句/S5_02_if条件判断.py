"""
if 语句用于单一条件测试
1> if
2> if-else
3> if-elif
4> if-elif-elif...
4> if-elif-else


省略else 代码块有时候会更有用

"""

age = 14

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:  # 使用elif来处理特殊情形会更清晰
    price = 5


# 测试多条件
# 如果这里使用if-else语句则会出现问题

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


# 使用循环来测试多条件, 提高效率

requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':   # 店里没有青椒了
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
