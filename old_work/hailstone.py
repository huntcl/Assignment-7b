# Author: Clara Hunt
# Github username: huntcl
# Date: 04/24/26
# Description: Returns the number of steps to reach 1 in a hailstone sequence.

def hailstone(num):
    """Return the number of steps to reach 1 in the hailstone sequence."""
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        steps += 1

    return steps