#even
number = [1,2,3,4,5,6,7,8,9,10]
def num(number):
    return number % 2 == 0
even_number = filter(num,number)
numbers = list(even_number)
print(numbers)

# odd
number = [1,2,3,4,5,6,7,8,9,10]
def num(number):
    return number % 2 == 1
odd_number = filter(num,number)
numbers = list(odd_number)
print(numbers)

# Strings by length
a = input("enter The Name : ")
def num(a):
    return len(a)
print("String Length : ",num(a))
# Calculate the sum of all numbers using lambda 
from functools import reduce
numbers = [1, 5, 3, 5, 10]
g = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", g)







