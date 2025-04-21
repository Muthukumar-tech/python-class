###print all the numbers from 1-15
##x = int(input(" Enter The Value : "))
##y = int(input(" Enter The Value : ")) 
##def print_(a,b):
##    for i in range(a,b):
##        print(i)
##
##print_(x,y)

###print odd numbers from 6-29
##a = int(input(" Enter The odd number checking Value : "))
##b = int(input(" Enter The odd number checking Value : "))
##def oddnum(x,y):
##    for i in range(x,y):
##        if i % 2 == 1:
##            print("odd number is : ",i)
##
##oddnum(a,b)

###print even numbers from 20-40.
##c = int(input("Enter The even number checking Value : "))
##d = int(input("Enter The even number checking Value : "))
##def evennum(a,c):
##    for n in range(a,c):
##        if n % 2 == 0:
##            print("Even Number is :",n)
##
##evennum(c,d)

####for divisible of 3 print ".  ".
##j = int(input("Enter The 3 divisible Checking Number : "))
##v = int(input("Enter The 3 divisible Checking Number : "))
##def divi(r,d):
##    for i in range(r,d):
##        if i% 3 == 0 and i % 5 == 0:
##            print(i,"its Divied By Both 3 and 5")
##        elif i % 5 == 0:
##            print(i,"it is divied by 5")
##        elif i% 3 == 0:
##            print(i,"it is divied by 3")
##        
##divi(j,v)

###print all the elements of an list.
##a = [1,54,15468,16524]
##def pri(c):
##    print(c)
##pri(a)

###calculate sum of all elements in an list
##h = [654,684,354,3541,574]
##def add(j):
##    total = 0
##    for i in j:
##        total += i
##        print("Total No: ", total)
##
##add(h)

###calculate the sum of all numbers from 1 to 100
##a = 1
##n = 100
##def sum_(b,c):
##    total = 0
##    for i in range(b,c):
##        total += i
##    print("Total No: ",total)
##
##sum_(a,n)

###calculate the factorial of a given number
##num=int(input("enter the number :"))
##def fact(x):
##    factorial=1
##    for i in range(1,num+1):
##        factorial*=i
##        print("Factorial:",factorial)
##fact(num)

#print a pattern of * in a triangle shape.
a =int(input("Enter The Number: ", ))
def pat(f):
    for i in range(f):
        for j in range(i+1):
            for k in range(i-5):
                print("* ",end=" ")
        print()
pat(a)

####find maximum element in an list.
##My_list = [1,9,8,15,101,1225,102]
##def max_(g):
##    max_element = g[0]
##    for num in g:
##        if num > max_element:
##            max_element = num
##    print("max number:",max_element)
##max_(My_list)
##
####find Fibonacci series of given number
##num=int(input("enter the number :"))
##def Fibonacci(x):
##    a,b=0,1
##    for i in range(num):
##        print(a, end=" ")
##        a,b=b,a+b
##    print()
##Fibonacci(num)
## 






              









        

