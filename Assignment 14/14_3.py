CheckGreater=lambda no1,no2:no1 if no1>no2 else no2 

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

result=CheckGreater(n1,n2)

print(f"The greater number between {n1} and {n2} is {result}")