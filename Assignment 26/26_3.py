class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter first value: "))
        self.Value2 = float(input("Enter second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed."
        return self.Value1 / self.Value2


def test_arithmetic(obj_name):
    print(f"\n--- Operating on {obj_name} ---")
    obj = Arithmetic()
    obj.Accept()

    print(f"Addition: {obj.Addition()}")
    print(f"Subtraction: {obj.Subtraction()}")
    print(f"Multiplication: {obj.Multiplication()}")
    print(f"Division: {obj.Division()}")


test_arithmetic("Object 1")
test_arithmetic("Object 2")