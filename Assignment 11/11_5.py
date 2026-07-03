num = int(input("Enter a number to check: "))

original_num = num
reversed_num = 0

if num < 0:
    print(f"{num} is not a palindrome number.")
else:
    while num > 0:
        remainder = num % 10                      
        reversed_num = (reversed_num * 10) + remainder 
        num = num // 10                             

    if original_num == reversed_num:
        print(original_num,"is a palindrome number")
    else:
        print(original_num,"is not a palindrome number")