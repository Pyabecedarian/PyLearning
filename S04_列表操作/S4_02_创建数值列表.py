# 函数 range() 生成一系列数字

for num in range(1, 5):
    print(num)


# range() 创建数字列表

numbers = list(range(1, 10, 2))
print(numbers)


# 创建一个列表, 包含1~10的平方

squares_list = []
for value in range(1, 10):
    square = value ** 2
    squares_list.append(square)

print(squares_list)


"""
列表解析

只需一行代码即可生成squares

格式:  列表名 = [表达式 for 循环]
!for 循环没有冒号!

"""

squares_list = [value **2 for value in range(1, 11)]

print(squares_list)
