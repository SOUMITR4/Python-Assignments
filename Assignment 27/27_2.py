class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")

    def Deposit(self, value):
        self.Amount += value
        print(f"Successfully deposited {value}. New Balance: {self.Amount}")

    def Withdraw(self, value):
        if value <= self.Amount:
            self.Amount -= value
            print(f"Successfully withdrew {value}. Remaining Balance: {self.Amount}")
        else:
            print(f"Insufficient funds! Withdrawal of {value} denied. Current Balance: {self.Amount}")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


if __name__ == "__main__":
    print("--- Account 1 Demo ---")
    acct1 = BankAccount("Alice Smith", 5000)
    acct1.Display()
    
    acct1.Deposit(1500)
    acct1.Withdraw(2000)
    
    interest_earned = acct1.CalculateInterest()
    print(f"Calculated Interest: {interest_earned}\n")

    print("--- Account 2 Demo (Insufficient Funds Test) ---")
    acct2 = BankAccount("Bob Jones", 1000)
    acct2.Display()
    acct2.Withdraw(1500)  