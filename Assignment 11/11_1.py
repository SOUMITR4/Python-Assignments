def CheckPrime():
    no=int(input("Enter a number to check if it is PRIME:"))
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            print("PRIME NUMBER")
        else:
            print("NOT PRIME NUMBER")

def main():
    CheckPrime()

if __name__ == "__main__":
    main()