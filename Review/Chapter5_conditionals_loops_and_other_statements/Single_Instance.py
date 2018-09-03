class Dog:
    dog_type = '狗'
    __init_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__init_instance:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self):
        if not Dog.__init_instance:
            self.name = '小花'
            Dog.__init_instance = True

    @staticmethod
    def drink():
        print("我要喝水")


dog1 = Dog()

print(dog1.name)
dog1.name = '小黑'
print(dog1.name)
dog2 = Dog()
print(dog1.name)
print(dog2.name)
print(dog1 is dog2)
