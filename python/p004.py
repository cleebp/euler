"""
Problem 4
Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largest_palin():
    palins = []
    for i in range(100,1000):
        for j in range(i+1, 1000):
            product = i * j
            if is_palin(int(product)):
                palins.append(product)

    return max(palins)

# helper method to return if given number is a palindrome
def is_palin(num):
    # reverse num and see if it still equals
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def main():
    palin = largest_palin()
    print("p004 answer:",palin)

main()
