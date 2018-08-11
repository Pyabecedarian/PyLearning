"""
S7_03中介绍了while循环移动列表中的元素案例

类似的, 可以通过函数来完成此操作


将列表传递给函数后, 函数就可以对其进行修改. 在函数中对这个列表所作的
任何修改都是 永久性的, 这种特性使能够高效的处理大量数据

例如:
一家为用户提交设计制作的3D打印模型公司. 将需要打印的设计存储在一个
列表中, 打印后移动到另一个列表中.

"""


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计, 知道没有未打印的设计为止
    :param unprinted_designs: 未打印设计列表
    :param completed_models: 打印完成的模型列表
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        current_design = current_design.title()

        if current_design[:2].lower() in ['ip', 'im']:
            c_str = ''
            for c in current_design:
                if c == 'I':
                    c = 'i'
                if c == 'p':
                    c = 'P'
                if c == 'm':
                    c = 'M'
                c_str += c
            current_design = c_str
            del c_str

        print("Printing model: " + current_design)

        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    显示所有已打印的模型

    :param completed_models: 打印完成的列表
    """

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("\t" + completed_model)


unprinted_designs = ['iphone case',
                     'robot pendant',
                     'dodecahedron',
                     'imac pro'
                     ]

completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()


# 禁止函数修改列表, 可将列表的副本传递给函数
# unprinted_designs_1副本传递给函数, 原列表不会发生变化

unprinted_designs_1 = ['mackbook pro',
                       'robot ring',
                       'dodecahedron',
                       'imac pro',
                       'ipad'
                       ]

completed_models_1 = []

print_models(unprinted_designs_1[:], completed_models_1)
show_completed_models(completed_models_1)
