# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def isPrime(number):
    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True

prime = []
i = 2

while len(prime) < 10000:
    i += 1
    if isPrime(i):
        prime.append(i)

print(prime[-1])
