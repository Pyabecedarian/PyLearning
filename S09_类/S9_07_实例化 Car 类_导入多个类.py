# 导入多个类
# from S9_类.Car import Car, ElectricCar


# *在一个模块中导入另一个模块*
from S09_类.ElectricCar import ElectricCar, Car


# 实例化电动汽车
my_tesla = ElectricCar('tesla', 'model x', 2016, 80)
my_tesla.description_car()

# my_tesla._battery_size.read_battery()
my_tesla.battery.read_battery()  # renamed "battery" as public
"""
[ my_tesla._battery. sth... ]

Warning:

Accessing a protected member (a member prefixed with _) of a class
from outside that class usually calls for trouble, since the 
creator of that class did not intend this member to be exposed.

Best Practice:
1>. Make sure that accessing the member from outside the class 
    does not cause any inadvertent side effects.
2>. Refactor it such that it becomes part of the public interface
    of the class.
"""

# 显示电池容量
my_tesla.battery.get_range()

# 升级电池容量
my_tesla.battery.upgrade_battery()

# 显示最新续航里程
my_tesla.battery.get_range()


# 实例化普通汽车
my_beetle = Car('volkswagen', 'beetle', 2017)
# 汽车简介
my_beetle.description_car()
