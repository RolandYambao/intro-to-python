'''
Define a function `is_prime(number)` that returns `True` if `number` is prime.
Otherwise, False. Assume `number` is a positive integer.

Examples:

is_prime(2); # => True
is_prime(10); # => False
is_prime(11); # => True
is_prime(9); # => False
is_prime(2017); # => True
'''

def is_prime(number):
    if (number == 1):
        return False
    if (number == 2):
        return True; 
    for i in range(2, number):
        if (number % i == 0):
            return False
        else:
            return True 
        
print(is_prime(2))
print(is_prime(10))
print(is_prime(11))
print(is_prime(9))
print(is_prime(2017))