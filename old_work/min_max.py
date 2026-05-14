# Author: Clara Hunt
# Github username: huntcl
# Date: 04/15/26
# Description: Identifies the minimum and maximum values from user-entered integers.

count = int(input("How many integers would you like to enter?"))

print("Please enter", count, "integers.")

# get first number
num= int(input())

min_val = num
max_val = num

# loop for remaining numbers
for index in range(count - 1):
    num = int(input())

    if num < min_val:
        min_val = num

    if num > max_val:
        max_val = num

print("min:", min_val)
print("max:", max_val)



