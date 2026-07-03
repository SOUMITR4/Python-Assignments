n = int(input("Enter how many numbers to print: "))

print(f"\nPrinting {n} numbers starting from 1 in reverse order:")

for i in range(n, 0, -1):
    print(i, end=" ")
