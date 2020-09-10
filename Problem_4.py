# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    str_number = str(number)
    reversed_number = str_number[::-1]
    return str_number == reversed_number


i = 999
j = 999

while isPalindrome(i * j) is not True:
    i -= 1
    if i % 10 == 0:
        j -= 1


print(f"i : {i} and j : {j}")
