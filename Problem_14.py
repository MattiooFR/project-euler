# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def make_chain(starting_number):
    working_number = starting_number
    count = 0
    while working_number != 1:
        if working_number % 2:
            working_number = working_number * 3 + 1
        else:
            working_number /= 2
        count += 1
    return (starting_number, count)


longest_count = 0
number = 999999
while number > 0:
    num, count = make_chain(number)
    if count > longest_count:
        print(f"Number {num} is the longest chain with : {count} terms")
        longest_count = count
    number -= 1
print("Finnish !")
