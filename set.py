# Create a Set
a = {"Sets","are written","with curly","brackets"}
print(a)

#Duplicate values will be Not Allowed
b = {123,8484,166,123}
c = {"rank = 1","name:john",True,1,False}
print(c)
print(b)
#access:
for i in a:
    print(i)
#check
print(1 in c)
print(2 not in c)
#add
a.add("kumar")
print(a)
#remove
c.remove(True)
print(c)
#update
number = {15,5827,6584,61}
a.update(number)
print(a)

#discard
b.discard(123)
print(b)
#pop
a.pop()
print(a)
#union
a = {"absara", "Dooms", "charp"}
b = {1, 2, 3}
c = a.union(b)
print(c)
bike = {"royal Enfelid","yamaha","bajaj"}
Spare = {"light","indicator","wheel"}
Buy = {"helmet"}
st = bike | Spare | Buy
print(st)
#update
num1 = {57,54,24,46,35}
num2 = {89,16,68,55,69}
num1.update(num2)
print(num1)
#intersection
set1 = {"apple","banana","dragon"}
set2 = {"cherry","musambi","apple"}

set3 = set1.intersection(set2)
print(set3)

#difference
set4 = set1.difference(set2)
print(set4)
#symmetric_difference
set5 = set1.symmetric_difference(set2)
print(set5)








