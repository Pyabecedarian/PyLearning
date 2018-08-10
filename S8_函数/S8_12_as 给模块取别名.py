# as 给模块取别名

import S8_函数.functions_ as f

f_name = f.get_formatted_name('albert', 'einstein')
print(f_name)


"""
导入模块中的所有函数 

    from module_name import *

可通过名称来调用每个函数, 而无需使用句点表示法

注: 使用非自己编写的大型模块时, 最好不要采用这么导入方法, 避免模块中函数与项目
中函数同名, 进而覆盖函数

"""
