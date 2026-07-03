def Table():
    no=int(input("Enter a number to generate its TABLE:"))
    for i in range(1,11,1):
        print(i*no)

def main():
    Table()

if __name__ == "__main__":
    main()