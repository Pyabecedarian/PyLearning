"""
1>.  使用 as 给函数 指定别名

如果要导入的函数的名称与程序中现有的名称有冲突,或者函数名称太长, 可使用as指定
简短而独一无二的别名---函数的另一个名称. 要这样做, 需要在导入时指定

    from module_name import function_name as fn

2>.  as 还可以给 模块 取别名

    import module_name as mn

"""

# as 给函数取别名
from S08_函数.functions_ import get_formatted_name as gfn

fm_name = gfn("albert", 'einstein')
print(fm_name)

# as 给模块取别名
