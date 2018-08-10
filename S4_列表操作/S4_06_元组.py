"""
不可变的列表 = 元组

tuple = (element1, element2,  ...)

"""


# 遍历元组

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)



# 修改元组变量
"""
虽然不能修改元组的元素, 但可以给存储元组的变量赋值
实际上相当于修改元组名这个引用, 使之指向另一个元组

dimensions = ( ,)
"""

dimensions = (200, 59)
print("\nThe original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)    # 修改这个引用, 使之指向另一个元组
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
