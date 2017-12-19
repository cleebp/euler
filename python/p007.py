"""
Problem 7
10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import math
import time

# prime helper method
def is_prime(n):
    # disregard even numbers greater than 2
    if n % 2 == 0 and n > 2:
        return False
    # only check up till square root of n, only check odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def n_prime(n):
    loop = True
    count = 0
    num = 2
    while loop:
        if is_prime(num):
            count = count + 1
        if count is n:
            break
        num = num + 1
    return num

def main():
    t1 = time.time()
    result = n_prime(10001)
    dT = time.time() - t1
    print("p007 answer:", result)
    print("time to compute:", dT)

main()
