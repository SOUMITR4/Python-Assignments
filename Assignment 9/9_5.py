def CheckDivisibilty():
    no=int(input("Enter a number to check wheter it is divisible by 3 and 5:"))
    if(no%3==0 and no%5==0):
        print("YES")
    else:
        print("NO") 

def main():
    CheckDivisibilty()

if __name__ == "__main__":
    main()