""""
如何拒绝顾客奇怪的配料要求??

可以将披萨店里的配料定义为一个列表(或元组), 顾客的要求定义另一个列表.
遍历时每次都将顾客的要求与店里已有的配料进行对比
"""


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping not in available_toppings:
        print("Sorry, we don't have " + requested_topping + "!")
    else:
        print("Adding " + requested_topping + ".")
print('\nFinished making your pizza!')
