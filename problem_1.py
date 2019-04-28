# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import math

def sum_cont(num):
    return (num * (num + 1)) / 2 

def prob_1(first, second, mcm, limit):
    sum_first  = sum_cont(math.trunc(limit / first)) * first
    sum_second = sum_cont(math.trunc(limit / second)) * second
    sum_mcm    = sum_cont(math.trunc(limit / mcm)) * mcm
    return sum_first + sum_second - sum_mcm

print(prob_1(3,5,15,1000))

