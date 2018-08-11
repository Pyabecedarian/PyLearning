# sort()方法 永久性排序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


# sorted()函数 临时排序

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars, reverse=True))

print("\nHere is the original list: ")
print(cars)


# 反转列表排序, reverse()方法

"""
假设汽车列表是按购买时间排列的,可轻松的按相反的顺序排列
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


# 函数len()确定列表长度len
print(len(cars))
