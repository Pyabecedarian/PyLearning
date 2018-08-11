"""
改版 ElectricCar类, 继承自 Car类,
但其关于电池属性, 由 Battery类 专门负责

"""


# import S9_类.S9_01_Car类 as c_Car
# import S9_类.S9_05_Battery类_实例作属性 as c_Battery
from S09_类.S9_01_Car类 import Car
from S09_类.S9_05_Battery类_实例作属性 import Battery


class ElectricCar(Car):
    """电动汽车的独特之处 --- 改版"""

    def __init__(self, make, model, year, battery_size=70, mileage=0,):
        """初始化父类, 再初始化电动汽车特有属性"""

        super().__init__(make, model, year, mileage)

        # 创建一个新的Battery实例
        self.battery = Battery(battery_size)  # 此处若设置为 protected,
        # 则后面调用read_battery()时将出现警告
