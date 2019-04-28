# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def prob_4(digits):
    maximal = 0
    max_arg = None
    for x in range(10**(digits - 1),10**digits):
        for y in range(10**(digits - 1),10**digits):
            num = x*y
            if num > maximal and is_palindrome(num):
                maximal = num
                max_arg = (x,y)
    return max_arg

print(prob_4(3))

