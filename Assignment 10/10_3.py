def Factorial():
    num=int(input("Enter a number:"))
    factorial=1
    for i in range(1,num+1):
        factorial *= i
    print(factorial)

def main():
    Factorial()

if __name__ == "__main__":
    main()