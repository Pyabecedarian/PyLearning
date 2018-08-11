"""
关键字实参

函数调用实参传递方式二: 关键字实参
调用时, 指定形参名

func_name(arg_1 = sth, arg_2 = sth ...)

这种方式调用, 显式的规定了实参传递的形参名, 因此调用时实参位置不重要

"""

# 导入模块
import S8_函数.functions_

# 关键字实参调用可以忽略形参的位置
S8_函数.functions_.describe_pet(pet_name='harry', animal_type='mouse')
