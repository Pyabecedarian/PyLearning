"""
2>.  导入模块中的特定函数(任意数量)

from module_name import function_0, function_1, function_2, ... ...

"""

# 导入 get_formatted_name()函数 并指定别名
from S08_函数.functions_ import get_formatted_name

formatted_name = get_formatted_name('albert', 'einstein')
print(formatted_name)
