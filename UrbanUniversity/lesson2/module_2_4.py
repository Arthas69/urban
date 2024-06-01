# Or we can use sqrt of num to make it quicker
# in function we use cycle FOR as in example below

# from math import sqrt
# for i in range(2, int(sqrt(n) + 1)):


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if is_prime(num):
        primes.append(num)
    else:
        not_primes.append(num)

print(f"Primes: {primes}", f"Not Primes: {not_primes}", sep='\n')
