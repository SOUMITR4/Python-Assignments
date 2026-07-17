class Demo:
    Value = 0

    def __init__(self, value1, value2):
        self.no1 = value1
        self.no2 = value2

    def Fun(self):
        print(f"Inside Fun - no1: {self.no1}, no2: {self.no2}")

    def Gun(self):
        print(f"Inside Gun - no1: {self.no1}, no2: {self.no2}")


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()