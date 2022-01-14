'''
Define a function `isPrime(number)` that returns `true` if `number` is prime.
Otherwise, false. Assume `number` is a positive integer.

Examples:

isPrime(2); // => true
isPrime(10); // => false
isPrime(11); // => true
isPrime(9); // => false
isPrime(2017); // => true
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
print(is_prime(3))
print(is_prime(5))
print(is_prime(10))