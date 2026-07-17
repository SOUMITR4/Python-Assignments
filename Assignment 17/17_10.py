def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Input: "))
print(f"Output: {sum_of_digits(num)}")