# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# from sympy.solvers import solve
# from sympy import Symbol

# a = Symbol("a")
# b = Symbol("b")
# c = Symbol("c")

# print(solve(a + b + c - 1000, a, b, c, dict=True))


a, b, c = 0, 0, 0


for c in range(300, 1000):
    for b in range(100, 500):
        for a in range(100, 500):
            if a ** 2 + b ** 2 == c ** 2:
                print("Found a pythagore solution: ", a, b, c)
                if a + b + c == 1000:
                    print("Found THE solution: ", a, b, c, "product is:", a * b * c)
