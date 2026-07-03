def printEven():
    no=int(input("Enter a number:"))
    for i in range(2,no+1,2):
        print(i,end="")
    print()

def main():
    printEven()
   

if __name__ == "__main__":
    main()