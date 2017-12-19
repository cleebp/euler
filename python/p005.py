"""
Problem 5
Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

def smallest_mult():
    result = 20
    found = False
    while not found:
        check = True
        for i in range(1,21):
            if result % i is not 0:
                result = result + 1
                check = False
                break
        found = check
    return result

def main():
    t1 = time.time()
    result = smallest_mult()
    t2 = time.time()
    dT = t2 - t1
    print("p005 answer:", result)
    print("time to compute:", dT)

main()
