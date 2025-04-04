#list task
#Calculate amounts in the list.
numbers = [1,8,51,254,18,948]
total = 0
for num in numbers:
    total += num
print("Total :", total)
## Find Max element in the List
a = [5,8,6,10,80]
bignumber = a[0]
for num in a:
    if num > bignumber:
        bignumber = num
print("max No:",bignumber)

 #Find Min element in the list.
z = [10,50,40,1,80]
smallnumber = z[0]
for n in z:
    if n < smallnumber:
        smallnumber = n
print("min No:",smallnumber)
 #PENDING TASK
number = [521,6591,51,6521,984,514]
odd_number = []
for num in number:
    if num % 2 ! = 0:
        odd_number.append(num)
print("odd original Number",number)
print("odd Number:",odd_number)

#EVEN TASK
even_number = []
for i in number:
    if i % 2 == 0:
        even_number.append(i)
print("Even original Number",number)
print("even number:",even_number)



