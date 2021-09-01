from math import isqrt


# Finding the primes using Sieve of Eratosthenes.
def primes_less_than(n: int) -> list[int]:
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [num for num in range(n) if is_prime[num]]


if __name__ == '__main__':
    number = 2000
    primes_list = primes_less_than(number)
    total = sum(primes_list)
    print(f"There are {len(primes_list)} prime numbers below {number} which are listed below:\n{primes_list}")
    print(f"The Sum of all the prime numbers below {number} is: {total}")
