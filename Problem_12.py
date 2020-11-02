# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
import math


def generate_natural_triangle(number):
    return sum(range(1, number + 1))


def count_divisor(number):
    count = 1
    i = 1
    while i <= math.sqrt(number):

        if number % i == 0:

            # If divisors are equal, print only one
            if number / i == i:
                count += 1
            else:
                # Otherwise print both
                count += 2
        i = i + 1
    return count


num = 2000

while count_divisor(generate_natural_triangle(num)) < 500:
    num += 1

print(count_divisor(generate_natural_triangle(num)), num)