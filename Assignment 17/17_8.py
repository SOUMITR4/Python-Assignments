def triangle_pattern(n):
    for i in range(1, n + 1):
        row = [str(j) for j in range(1, i + 1)]
        print(" \t".join(row))

num = int(input("Input: "))
print("Output:")
triangle_pattern(num)