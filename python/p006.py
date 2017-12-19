"""
Problem 6
Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def squares():
    sum_squares = 0
    sums = 0
    for i in range(1,101):
        sum_squares = sum_squares + i**2
        sums = sums + i
    sums = sums**2
    result = sums - sum_squares
    return result
    
def main():
    result = squares()
    print("p006 answer:",result)

main()
