##def is_prime(n):
##    if n <= 1:
##        return False
##    for i in range(2, n):
##        if n % i == 0:
##            return False
##    return True
##
##num = int(input("Enter a number: "))
##
##if is_prime(num):
##    print("Prime number")
##else:
##    print("Not a prime number")
##
##duplicate
num = [6,5,8,1,2,8,5,3,6,2]
original =[]
duplicate =[]
def sum_(n):
    for i in n:
        if i not in original:
            original.append(i)
        else:
            if i not in duplicate:
                duplicate.append(i)
sum_(num)

print("Original:", original)
print("Duplicates:", duplicate)

        
        
