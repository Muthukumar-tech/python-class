#Tuple Task
#Calculate amounts in the list.

a = (65,9846,8716,68,164416)
total = 0
for i in a:
    total += i
print("Total no:",total)

# Find Max element in the List

n = (214,657,618,176,3982)
high = 0
for x in n:
    if x > high:
        high = x
print("High No:",high)

# Find min element in the list.

f = (1460,36817,849,659,365,2329)
low = f[0]
for b in f:
    if b < low:
        low = b
print("low No:",low)

#Add Odd Number in another list from original list.
m = (264,36817,194,650,1478)
odd_number =[]
for w in m:
    if w % 2 != 0:
        odd_number.append(w)
print("odd number:",odd_number)

#Add even Number in another list from original list.
even_number =[]
for y in m:
    if y % 2 == 0:
        even_number.append(y)
print("even Number:",even_number)



