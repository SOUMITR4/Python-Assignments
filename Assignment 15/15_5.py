from functools import reduce

numbers=[3,1,9,4,5]

max=reduce(lambda x,y:x if x>y else y,numbers)

print(max)