
fib_cache = {}

def fib(n):
    # If n is present in cache then return it
    if n in fib_cache:
        return fib_cache[n]

    #raise error if n is not a positive int
    if n != int:
        raise TypeError("n must be a positive int!")
    if n < 1:
        raise ValueError("n must be a positive int!")

    #Compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1) + fib(n-2)

    #Cache the value and return it
    fib_cache[n] = value
    return value

for n in range(1, 26):
    print(n, ":", fib(n))


#Using inbuilt python library LRU_CACHE
from functools import lru_cache

@lru_cache(maxsize=1000)
# raise error if n is not a positive int

def fib(n):
    if n != int:
        raise TypeError("n must be a positive int!")
    if n < 1:
        raise ValueError("n must be a positive int!")

    # Compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

for n in range(1, 26):
    print(n, ":", fib(n))