#### add and even 
##n = int(input())
##
##if n % 2 == 0:
##    print("Its a even number")
##else:
##    print("Its a even number")


###compare 2 numbers and display the largest numbers
##usernumber1 = int(input("Enter the 1st number: "))
##usernumber2 = int(input("Enter the 2nd number: "))
##
##if usernumber1 > usernumber2:
##    print("The largest number is:", usernumber1)
##elif usernumber2 > usernumber1:
##    print("The largest number is:", usernumber2)
##else:
##    print("Both numbers are equal.")

### check the number positive, nagative or zero
##
##number = int(input("enter a number : "))
##
##if number > 0:
##    print("the number is a positive")
##elif number < 0 :
##    print("the number is a nagative")
##else :
##    print("the number is a zero")
    
####determines the type of triangle based on the side length.
##
##           # equilateral, isosceles or scalene.
##
##x = int(input(" x its a = "))
##y = int(input(" y its a = "))
##z = int(input(" z its a = "))
##
##if x == y == z:
##    print("its a equilateral triangle")
##
##elif x == y or y == z or x == z:
##    print("its a isosceles triangle")
##
##else :
##    print(" its a scalene triangle")

###write a program that calculate the grade with use of given percentage
##percentage = int(input("enter my percentage: "))
##if percentage >= 90:
##    grade = "A"
##elif percentage >= 80:
##    grade = "B"
##elif percentage >= 70:
##    grade = "C"
##elif percentage >= 60:
##    grade = "D"
##else:
##    grade = "f"
##    
##print("my grade is:",grade )

### determines the season, based on a given month
##
##month = (input())
##
##if month in ("dec","jan","feb"):
##    print("winter")
##elif month in ("mar","apr","may"):
##    print("spring")
##elif month in ("jun","jul","aug"):
##    print("summer")
##else :
##    print("autuum")


##int_number = 1000
##float_number = 10.25
##new_number =int_number+float_number
##
##
##print("value:",new_number)
##print("data type",type(new_number))
##
##x = False
##y = str(x)
##print(type(y))
##
##n2 = 100
##n1 = str(n2)
##print ( type( n1))
##
##x1 = "1000"
##x2 = float(x1)
##print(type(x2))


####check three person salary and display the minimum salary 
##
##person1 = int(input("enter  person 1 salary : "))
##person2 = int(input("enter  person 2 salary : "))
##person3 = int(input("enter  person 3 salary : "))
##
##min_salary = min(person1, person2, person3)
##
##print("the minimum salary is a",min_salary)


### conditional statements
##
##age = int(input("its My Age :"))
##
##if age < 12:
##    print("child")
##
##elif age < 19:
##    print("teenager")
##
##elif age < 35:
##    print("young adult")
##
##else :
##    print("adult")

       #19.02.2025
       #determines the type of triangle based on the side length.
##
##           # equilateral, isosceles or scalene.
       # match cases
### check if the number is odd or even.
##
##n1 = int(input(" Enter your number: "))
##match  n1 % 2 == 0:
##    case True:
##        print(" n1 is even")
##    case false:
##        print(" n1 is odd")


###compare 2 numbers and display the largest number
##        
##a = int(input(" Enter a number 1: ",))
##b = int(input(" Enter a number 2: ",))
##
##match a < b :
##    case True:
##        print(" a is lesser  than ")
##    case False:
##        print(" a is graeter  than ")

     #04.03.2025
      
####print all the numbers from 1-15.
##
##for i in range(1,16):
##    print(i)


#####print odd numbers from 6-29.
##for i in range(6,30):
##    if i % 2 != 0:
##        print(i)


#print all the elements of an list.

##list_ =["banana","apple","munch","batterys"]
##for n in list_:
##    print(list_)


## #calculate sum of all elements in an list
##a = [10,20,30]
##total = 0
##for i in a: 
##      total += i
##print("sum:",total)
## 



 #calculate the sum of all numbers from 1 to 100
##total=0
##for i in range(1, 101):
##      total += i
##print("sum:",total)


####For divisible Of 3 and 5
##for i in range(1,15):
##    if i % 3 == 0 and i % 5 == 0:
##        print(".")
##    elif i % 3 == 0:
##        print(".")
##    elif i % 5 == 0:
##        print(".")
##    else:
##        print(i)
####
###for divisible of 3
##
##for i in range(1,15):
##    if i % 3 == 0:
##        print(".")
##    else:
##        print(i)
##
# for divisible of 5

##for i in range(1,15):
##    if i % 5 == 0:
##        print("its Equl")
##    else:
##        print(i)
##
## 
##find maximum element in an list.

##My_list = [1,9,8,15,101,1225,102]
##max_element = My_list[0]
##for num in My_list:
##    if num > max_element:
##        max_element = num
##print("max_element:",max_element)

##print a pattern of * in a triangle shape.

##for i in range(5):
##    for j in range(5):
##        print("*",end=" ")
##    print()

##for i in range(5):
##    for j in range(i):
##        print(" ",end=" ")
##    for j in range(i,5):
##        print("*",end=" ")
##    print()

##for i in range(5):
##    for j in range(5,i,-1):
##        print(" ",end=" ")
##    for k in range(i+1):
##        print("*",end=" ")
##    print()
n = 5
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("* ",end="  ")
    print()




    





