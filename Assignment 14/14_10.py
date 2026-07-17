CheckLargest=lambda a,b,c:a if(a>b and a>c ) else (b if b>c else c)

no1=int(input("Enter first number:"))
no2=int(input("Enter second number:"))
no3=int(input("Enter third number:"))

result=CheckLargest(no1,no2,no3)

print(f"Largest number from {no1},{no2},{no3} is {result}")