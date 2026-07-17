number=[15,3,5,30,45,20]

divby_3_5=list(filter(lambda x: x%3==0 and x%5==0,number))

print(divby_3_5)