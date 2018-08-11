"""
随着类中的细节越来越多, 属性和方法清单及文件都越来越长

这种情况下, 可以将类的一部分作为一个独立的类提取出来.

将大型类拆分成多个协同工作的小类.

Battery类实例 用作 ElectricCar类 的一个属性, 专门针对电瓶的属性和方法
"""


class Battery:
    """一次模拟电动汽车电池的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电池的属性"""

        self._battery_size = battery_size

    def read_battery(self):
        """读取电池电量"""

        print("This car has a " + str(self._battery_size) +
              "-kWh battery")

    def get_range(self):
        """报告电池的续航里程"""

        _range = None  # 预先定义局部变量, 否则出现警告

        if self._battery_size == 70:
            _range = 240
        elif self._battery_size == 80:
            _range = 270
        elif self._battery_size == 85:
            _range = 290

        msg = "This car can go approximately " + str(_range)
        msg += " miles on a full charge."

        print(msg)

        """
        _range 应在 if-elif 之前定义, 否则出现警告: 
        'Local variable might be referenced before assignment'.
        
        Reason:
        
        This is because the linter sees that _range is assigned values 
        inside if-elif conditions. however, the linter cannot know that 
        these if-elif conditions are complementary. 
        So, considering the case when none of the conditions is true, 
        the variable _range will end up uninitialized.
        
        Best Practice:
        
        To get rid of this warning, you can simply initialize the 
        variable before any of the if conditions with None value
        
        """

    def upgrade_battery(self):
        """升级电池容量到85-kWh"""

        if self._battery_size != 85:
            self._battery_size = 85
            print("\nBattery upgraded. Battery size is now " +
                  str(self._battery_size) + "-kWh.")
        else:
            print("\nBattery size is now 85-kWh, no need to upgrade.")
