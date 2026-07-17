def div_by_5(num):
    if num%5==0:
        return True
    else:
        return False
    
number=int(input("Enter a number:"))
print(div_by_5(number))