"""
使用列表时避免索引错误

IndexError: list index out of range

"""

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])


"""
访问最后一个元素时,都可以使用索引-1. 即便列表长度发生变化依然有效.

仅当列表为空时, 才会报错.
"""

# motorcycles = []
# print(motorcycles[-1])
