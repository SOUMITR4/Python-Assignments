no=int(input("Enter a number: "))
temp = abs(no)
digit_sum = 0

while temp > 0:
    remainder = temp % 10   
    digit_sum += remainder 
    temp = temp // 10

print("Sum of digits:",digit_sum)