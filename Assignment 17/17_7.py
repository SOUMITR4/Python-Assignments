def grid_pattern(n):
    row_pattern = " \t".join(str(i) for i in range(1, n + 1))
    for _ in range(n):
        print(row_pattern)

num = int(input("Input: "))
print("Output:")
grid_pattern(num)