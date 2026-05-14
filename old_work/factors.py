# Author: Clara Hunt
# Github username: huntcl
# Date: 04/15/26
# Description: Prints all factors of a positive integer.

num = int(input("Please enter a positive integer: "))

print("The factors of", num, "are:")

for index in range(1, num + 1):
    if num % index == 0:
        print(index)

