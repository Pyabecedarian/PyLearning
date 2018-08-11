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


"""
元组 - 重要应用场景 --- 组包, 拆包

1>. 组包

当把多个值赋值给一个变量时, Python 自动将多个值组包为一个元组

    a = 10, 20  
    # 此时 a = (10, 20)
    
2>. 拆包

当把元组赋值给多个变量时(变量的数量等于元组中元素的个数), Python 自动将元组拆包, 将各个元素
按顺序分别赋值给多个变量

    tuple = (10, 20)
    
    a, b = tuple  #拆包, 此时 a = 10, b = 20

"""


# Swap two numbers

a = 10
b = 20
print("\nBefore swapping: ")
print("a is: %d\nb is: %d" % (a, b))

a, b = b, a  # Swap numbers
print("\nAfter swapping: ")
print("a is: %d\nb is: %d" % (a, b))


"""
交换原理:
    
    a, b = b, a
    
    # = 右边有多个值, Python将自动组包为一个元组, 当赋值给 = 左边时, 左边是多个变量,
    # 因此python将自动拆包, 将元组中的值分别赋值给左边的变量
    
"""