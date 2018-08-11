"""
json 能将简单的Python数据转储到文件

JSON (JavaScript Object Notation)
(被包括Python在内的众多语言采用)

1>.  使用json.dump()和 json.load()

"""

# 导入 json 模块
import json

numbers = [2, 3, 5, 7, 11, 13]

# 写入数字
f_name = 'numbers.json'
with open(f_name, 'w') as f_obj:
    json.dump(numbers, f_obj)


# 读取数字
f_name = 'numbers.json'
with open(f_name) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
