def StarPattern(n):
    for i in range(n, 0, -1):
        print("* \t" * i)

num = int(input("Input: "))
print("Output:")
StarPattern(num)