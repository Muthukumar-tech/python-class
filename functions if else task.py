##determines the season, based on a given monthdef add(a,b):


number = int(input("its a value: "))
def oddnum(number):
    if number % 2 == 0:
        print("its a even")
    else:
        print("its a odd")
oddnum(number)
##compare 2 numbers and display the largest number.
a = int(input("its a value A : "))
b = int(input("its a value B : "))
def bignum(a,b):
    if a > b:
        print("A is Big Number")

    else:
        print("B is Small Number")
bignum(a,b)
##write a program that calculate the grade with use of given percentage.
percentage = float(input("enter my percentage: "))
def rank(percentage):
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "Fail"
    print("its  Grade: ",grade)
rank(percentage)

##determines the type of triangle based on the side length.

a = int(input("Its A Value : "))
b = int(input("Its B Value : "))
c = int(input("Its C Value : "))
def tri(a,b,c):
    if a == b == c:
        print("its a equilateral triangle")
    elif a == b or b == c or c == a:
        print("its a isosceles triangle")
    else:
        print("its a scalene triangle")
tri(a,b,c)
        
##determines the season, based on a given month
month = str(input("its a Month: "))
def season(month):
    if month in ("dec","jan","feb"):
        print("winter")
    elif month in ("mar","apr","may"):
        print("spring")
    elif month in ("jun","jul","aug"):
        print("summer")
    else:
        print("autuum")
season(month)

##check three person salary and display the minimum salary 

person1 = int(input("Enter  Person 1 Salary : "))
person2 = int(input("Enter  Person 2 Salary : "))
person3 = int(input("Enter  Person 3 Salary : "))

def salary(person1,person2,person3):
    min_salary = min(person1, person2, person3)
    print("The Minimum Salary is A : ",min_salary)

salary(person1,person2,person3)

## check the number positive, nagative or zero

number = int(input("Enter The Number : "))
def num(number):
    if number > 15:
        print(" This Number is Positive")
    elif number > 10:
        print("This Number is Nagative")
    else:
        print("Its Zero")

num(number)







