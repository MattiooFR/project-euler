# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?


# def divisible(number):
#     return all([not bool(number % i) for i in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]])


# _ = 2520

# while divisible(_) is False:
#     _ += 1

# print(f"Smallet divisible number {_}")

# DOESN'T WORK, TOO SLOW

# Solution is to use PPCM in maths, we need to decompose each numbers in primary numbers
# and then multiply all of them together by the number with the biggest exponent

# 4=2^2
# 6=2⋅3
# 8=2^3
# 9=3^2
# 10=2⋅5
# 12=2^2⋅3
# 14=2⋅7
# 15=3⋅5
# 16=2^4
# 18=2⋅9
# 20=2^2⋅5

# So 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
