# 1> 使用del 语句 [可删除任意位置的元素]

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)  # 删除后,原来的值无法再访问了


# 2> 使用pop() [删除列表末尾的元素]

motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


"""

假设列表中摩托车是按时间存储的,就可以使用pop()打印一条消息,
指出最后购买的是那一款

"""

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + '.')


# 3> 弹出任意位置元素

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')


# 4> 根据值删除元素

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)
