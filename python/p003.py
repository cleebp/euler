"""
Problem 3
Largest prime factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def max_factors(num):
    i = 2
    # largest prime factor will never be larger than the square root of num
    while i * i < num:
        while num % i == 0:
            num = num / i
        i = i + 1
    return num

def main():
    max_factor = max_factors(600851475143)
    print("p003 answer:",max_factor)

main()
