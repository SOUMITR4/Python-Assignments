def FactorSum(n):
    total=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            total+=i
    return total
    
num=int(input("INPUT:"))
print("OUTPUT:",FactorSum(num))