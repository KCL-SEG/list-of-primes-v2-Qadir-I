"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2

    if number_of_primes <= 0:
        raise ValueError
    
    while len(list) < number_of_primes:
        prime = True
        
        for i in range(2, number):
            if number % i == 0:
                prime = False
        
        if prime:
            list.append(number)
        number += 1

    return list
