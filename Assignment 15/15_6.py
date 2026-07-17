from functools import reduce 

numbers=[3,1,9,-2,5]

min=reduce(lambda x,y:x if x<y else y,numbers)

print(min)