# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def is_divisible(num, divisors):
    for div in divisors:
        if num % div == 0:
            return True
    return False

def gen_prime():
    prime_list = []
    current = 2
    while True:
        prime_list.append(current)
        yield current
        while is_divisible(current, prime_list): current += 1 
            
def prob_3(target):
    prime_generator = gen_prime()
    prime = None
    while target != 1:
        prime = next(prime_generator)
        while target % prime == 0:
            target /= prime
    return prime      

print(prob_3(600851475143))
