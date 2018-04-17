# Write a program that returns the largest number-palindrome, which is the product of two prime five-digit numbers
# and returns the multipliers themselves.
# A prime number is a natural number that is divisible only by 1 and itself (2, 3, 5, 7, 11, ...).
# A palindrome is a string that is read equally in both directions (for example, ABBA).

import time
from itertools import combinations_with_replacement
from itertools import compress
import math

start = time.time()


def primeGen(num_limit):
    """A function which finds all the primes in range from 2 to N (num_limit)."""
    a = [True] * num_limit  # Initializing the list.
    a[0] = a[1] = False  # Both 0 and 1 are NOT prime numbers!
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, num_limit, i):  # Mark factors non-prime
                a[n] = False


def divisorGen(n):
    """A function which finds the divisors of a given integer.
    It doesn't return 1 and given integer as answers."""
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and i != n and i != 1:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def main():
    Primes = primeGen(100000)
    FiveDigitPrimes = [i for i in Primes if i >= 10000]
    Multiplications = [i*j for i, j in combinations_with_replacement(FiveDigitPrimes, 2) if str(i*j) == str(i*j)[::-1]]
    TrueIndexes = list(compress(range(len(Multiplications)), Multiplications))
    Palindromes = [Multiplications[i] for i in TrueIndexes]
    Result = max(Palindromes)
    Divisors = divisorGen(Result)
    print("The largest number-palindrome is: " + str(Result))
    print("The multipliers are: " + str(list(Divisors)))
main()

# Extra - measuring the time.
end = time.time()
time = end - start
print("It took exactly: " + str(time) + " seconds.")
