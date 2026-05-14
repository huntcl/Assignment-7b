# Author: Clara Hunt
# Github username: huntcl
# Date: 05/13/26
# Description: Uses recursion to multiply two positive integers.

def multiply(num1, num2):
    """
    Returns the product of two positive integers using recursion.
    """

    if num2 == 1:
        return num1

    return num1 + multiply(num1, num2 - 1)
