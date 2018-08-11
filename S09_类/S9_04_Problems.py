"""
Python 2.7中的继承

语法稍有不同
"""

"""
class Car(object)
    def __init__(self, make, model, year):
    --snip--
    

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        --snip
"""
