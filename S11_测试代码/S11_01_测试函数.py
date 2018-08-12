"""
文件夹 S8_函数中 functions_.py 中包括了一个简单的函数
    get_formatted_name()
现对其进行测试



"""
from S08_函数.functions_ import get_formatted_name
import unittest

# print("Enter 'q' at any time to quit." )
# while True:
#     first = input("First name: ")
#     if first == 'q':
#         break
#     second = input("Second name: ")
#     if second == 'q':
#         break
#
#     formatted_name = get_formatted_name(first, second)
#     print("\tNeatly formatted name is " + formatted_name + '.')

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理下像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')


    