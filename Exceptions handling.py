# 1. Handle Division by Zero
try:
    a = int(input("Enter The Number : "))
    b = int(input("Enter The Number : "))
    result = a / b 
    print("Result",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 2. Catch Multiple Exceptions
a = 1
name  = "hello"
def func(a):
    re = a + name 
    print(re)
try:
    func(a)
except(TypeError)as e:
    print(e)
except(UnboundLocalError) as e:
    print(e)

# 3. Using else with 
a = 1
strs = 15

def func(a):
    res = a + strs
    print(res)

try:
    func(a)
except TypeError as e:
    print(e)
except UnboundLocalError as e:
    print(e)
else:
    print("Function executed successfully without exceptions.")

# 4. Using finally block
try:
    x > 3
except:
    print("something Went Wrong")
else:
    print("nothing Went Wrong")
finally:
    print("The try...except block is finished")

# 5. Raise an Exception Manually
x = -1

if x < 10:
    raise Exception("Sorry, no numbers below zero")

# 6. Create and Handle a Custom Exception
try:
    num = 10/0
    print("Result:",num)
except:
    print("custom exception:")

# 7. Catch All Exceptions (Generic)
try:
    name = int(input("Not a Number : "))
except ValueError   : 
    print("something wrong Its Not a name ")

# 8. Try Opening a Non-existent File
try:
  with open("New e.txt","r") as file:
    show = file.read()
except FileNotFoundError:
    print(" its a Non-existent File")

# 9. Convert String to Int Safely 
user_input = input("Enter The Number: ")
try:
    num = int(user_input)
    print("you entered : ",num)
except ValueError :
    print("That's not a number !")

# 10. List Index Error Handling
mylist = [2154,8,25137]
try:
  a = int(input("Enter The number: "))
  print("Value Of The Index",mylist[a])
except IndexError:
  print("Oops! That index is out of range.")
except ValueError:
  print("Please enter a valid number.")

# 11. KeyError in Dictionary
my_dict = {"name": "kumar", "age": 25}

try:
    print(my_dict["gender"]) 
except KeyError:
    print("Key not found in dictionary.")

# 12. Attribute Error
x = "hello"

try:
    x.append("!")
except AttributeError:
    print("this is A AttributeError")

# 13. Import Error
try:
    from math import fake_function
except ImportError:
    print("its a ImportError ")
 
# 14. Type Error
x = input("Enter Any NUmber : ")
y = int(input("Enter The Any Other Value : "))
try:
  result = x + y
except TypeError:
    print("Typing Error :")
# 15. Nested Try-Except

def nestedvalue():
    a = input("Enter The Number : ")
    try:
        x = int(a)
        try:
            result = x / 0  # This will raise ZeroDivisionError
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    except ValueError:
        print("Invalid integer conversion.")

nestedvalue()

# 16. Loop with Exception Handling
for val in ["150", "0", "abc"]:
    try:
        print(100 / int(val))
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)
# 17. Handling IOError
try:
    with open('file.txt', 'r') as file:
        dd = file.read()
except IOError:
    print("Could not open the file")

# 18. Multiple Except with Single Block
try:
    x = int(input("Enter a number: "))
    result = 100 / x  
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Success! The result is {result}")

# 19. Handling Input Exception in Function
def number():
    try:
      return int(input("Enter a name : "))
    except ValueError:
      print("Invalid number")
number()
# 20. Retry Until Success
while True:
    try:
      age = int(input("Enter your age: "))
      if age < 18:
        print("you are under 18")
      else:
        print("Age verified")
        break
    except ValueError:
        print(" Please enter a valid age.")