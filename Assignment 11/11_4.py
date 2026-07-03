no=int(input("Enter a number:"))
is_negative = no < 0
temp = abs(no)
reversed_num = 0

while temp > 0:
    remainder = temp % 10              
    reversed_num = (reversed_num * 10) + remainder  
    temp = temp // 10                    


if is_negative:
    reversed_num = -reversed_num

print(f"Reversed number: {reversed_num}")