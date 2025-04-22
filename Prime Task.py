#prime Number 
for num in range(0,50):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# Palindrome
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Duplicate:

nums = [1, 2, 3, 2,4,5,6,4,2,3,7, 4, 5, 1]

duplicates = []
for i in nums:
    if nums.count(i) >  1 and i not in duplicates:
        duplicates.append(i)

print("Duplicates:", duplicates)

