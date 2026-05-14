# Author: Clara Hunt
# Github username: huntcl
# Date: 04/07/26
# Description: Calculates the minimum number of coins for the amount of cents entered by the user

print("Please enter an amount in cents less than a dollar.")

cents = int(input())

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickles = cents // 5
cents = cents % 5

pennies = cents

print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickles)
print("P:", pennies)