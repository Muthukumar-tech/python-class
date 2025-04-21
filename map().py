from functools import reduce
# # map() usage
nums = [1, 2, 3]
mapped = list(map(lambda x: x + 10, nums))
print("3:", mapped)

# #  Squre of map()
def squre(a):
    return a*a
number = (654,1,684)
num1 = map(squre,number)
num2 = tuple(num1)
print("THis Is The Squre No :",num2)

# Add Multiple Lists using map() and lambda
a = [6,65,67,84,36]
b = [32,42,21,145]
result = map(lambda x , y : x + y , a,b)
print(list(result))

# Multiple all element in a list
num1 = [368,149,684,36541,36514]
mul = reduce(lambda a , b : a * b , num1)
print(mul)

# convert in a string value upper case in a list
b = ["kumar"]
def name(a):
    return a.upper()
result = map(name,b)
print(list(result))

# calculates the product of two elements

def product(x,y):
    return x*y
ans = reduce(product, [2, 5, 3, 7])
print(ans)