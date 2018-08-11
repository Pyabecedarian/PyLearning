class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year, mileage=0):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._gas = 0

    def __str__(self):
        msg = ("This car is a " + str(self._year) +
               self._make.title() +
               self._model.title())
        return msg

    def description_car(self):
        """车辆简要说明"""

        print('\n\n' + str(self._year) + " " + self._make.title() + " " +
              self._model.title() + '\n\n')

    def read_odometer(self):
        """显示里程"""

        print("This car has " + str(self._mileage) +
              " miles on it.")

    def odometer_update(self, mileage):
        """更新里程"""

        if mileage < self._mileage:
            print("\n\tYou can't roll back an odometer!")
            return

        self._mileage = mileage
        print("\nMileage reset to " + str(mileage) + " miles.")
        self.read_odometer()

    def odometer_increment(self, mileage):
        """增加里程"""

        if mileage < 0:
            print("\n\tYou can't roll back an odometer!")
            return

        self._mileage += mileage
        print("\nMileage increased " + str(mileage) + " miles.")
        self.read_odometer()

    def fill_gas_tank(self):
        """添加汽油"""

        while True:
            gas_fill = input("\n\nHow much gas do you want to fill: ")
            if int(gas_fill) < 0:
                print("Sorry, please input a positive integer number.")
            else:
                self._gas += int(gas_fill)
                print(gas_fill + "L gas has restored.")
                print("Totally gas: " + str(self._gas) + "L")
                break
