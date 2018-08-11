import S9_类.S9_01_Car类 as Class_Car

# 创建对象
my_car = Class_Car.Car('audi', 'a4', 2016)

# 显示车信息
my_car.description_car()

# 显示车里程数
my_car.read_odometer()

# 更新里程
my_car.odometer_update(20000)

# 增加里程
my_car.odometer_increment(254)

# 尝试重新设置里程数
my_car.odometer_update(100)

# 添加汽油
my_car.fill_gas_tank()
