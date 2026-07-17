def count_digits(n):
    # Using string conversion handles large numbers effortlessly
    return len(str(abs(n)))

num = int(input("Input: "))
print(f"Output: {count_digits(num)}")