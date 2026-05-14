# Author: Clara Hunt
# Github username: huntcl
# Date: 05/13/26
# Description: Returns a list of all prime numbers up to and including a limit.

def list_of_primes_up_to(limit=100):
    """
    Returns a list of all prime numbers up to and including a limit.
    """
    prime = [True] * (limit + 1)

    if limit >= 0:
        prime[0] = False

    if limit >= 1:
        prime[1] = False

    for number in range(4, limit + 1, 2):
        prime[number] = False

    divisor = 3

    while divisor <= limit ** 0.5:
        if prime[divisor]:
            for number in range(divisor + divisor, limit + 1, divisor):
                prime[number] = False

        divisor += 1

    return [index for index in range(len(prime)) if prime[index]]
