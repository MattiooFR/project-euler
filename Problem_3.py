# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# def isPrime(number):
#     for i in range(2, number-1):
#         if number % i == 0:
#             return False
#     return True

n = 2
e = 600851475143
while e != 1:
    if e % n == 0:
        e = e / n
    else:
        n = n + 1
print(n)
