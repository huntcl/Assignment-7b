# Author: Clara Hunt
# Github username: huntcl
# Date: 04/24/26
# Description: Returns the nth Fibonacci number.

def fib(num):
    """Return nth Fibonacci number."""
    if num == 1 or num == 2:
        return 1

    prev = 1
    curr = 1

    for count in range(3, n + 1):
        next_val = prev + curr
        prev = curr
        curr = next_val

    return curr
