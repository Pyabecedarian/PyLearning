"""
利用 继承

创建一个 ElectricCar 类, 使其自动获得 Car 类的所有属性和方法

"""

# 导入Car类
import S9_类.S9_01_Car类 as Class_Car


class ElectricCar(Class_Car.Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year, mileage=0, battery=70):
        """初始化父类的属性
        再初始化电动汽车特有的属性
        """

        # super是一个特殊函数, 帮助Python将父类和子类关联起来.让Python调用父类
        # 的方法 __init__(), 让子类实例包含父类的所有属性
        super().__init__(make, model, year, mileage)
        self._battery_size = battery  # 电动汽车独有

    def read_battery(self):
        """读取当前电池容量"""

        print("This car has a " + str(self._battery_size) +
              "-kWh battery.")

    def fill_gas_tank(self):
        """电动车没有油箱"""

        print("\nThis car doesn't need a gas tank!\n")


my_tesla = ElectricCar('tesla', 'model x', 2017)

# 车辆介绍
my_tesla.description_car()

# 显示里程
my_tesla.read_odometer()

# 显示电量
my_tesla.read_battery()

# 增加里程
my_tesla.odometer_increment(1000)

# 尝试添加汽油
my_tesla.fill_gas_tank()
