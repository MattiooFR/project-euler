# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
import math


def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


primes = []
idx = 0

while idx < 2000000:
    if isPrime(idx):
        primes.append(idx)
    if idx % 1000 == 0:
        print(idx)
    idx += 1

print(sum(primes))
