def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Input: "))
if is_prime(num):
    print("Output: It is Prime Number")
else:
    print("Output: It is not a Prime Number")