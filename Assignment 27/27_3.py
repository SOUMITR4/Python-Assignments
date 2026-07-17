class Numbers:

    def __init__(self, value):
        self.Value = int(value)

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        if self.Value <= 1:
            return False
        
        sum_divisors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_divisors += i
                
        return sum_divisors == self.Value

    def Factors(self):
        print(f"Factors of {self.Value}: ", end="")
        factors_list = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors_list.append(i)
        print(", ".join(map(str, factors_list)))

    def SumFactors(self):
        total_sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total_sum += i
        return total_sum


if __name__ == "__main__":
    print("--- Testing Number: 7 ---")
    num1 = Numbers(7)
    print(f"Is Prime? {num1.ChkPrime()}")
    print(f"Is Perfect? {num1.ChkPerfect()}")
    num1.Factors()
    print(f"Sum of Factors: {num1.SumFactors()}\n")

    print("--- Testing Number: 6 ---")
    num2 = Numbers(6)
    print(f"Is Prime? {num2.ChkPrime()}")
    print(f"Is Perfect? {num2.ChkPerfect()}")
    num2.Factors()
    print(f"Sum of Factors: {num2.SumFactors()}\n")

    print("--- Testing Number: 12 ---")
    num3 = Numbers(12)
    print(f"Is Prime? {num3.ChkPrime()}")
    print(f"Is Perfect? {num3.ChkPerfect()}")
    num3.Factors()
    print(f"Sum of Factors: {num3.SumFactors()}")