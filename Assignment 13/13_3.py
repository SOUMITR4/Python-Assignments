num = int(input("Enter a number to check: "))

if num <= 0:
    print(f"{num} is not a perfect number.")
else:
    divisor_sum = 0
    
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print(num,"is a perfect number!")
    else:
        print(num,"is not a perfect number.")