def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return is_prime

limit = 1000000
primes = sieve_of_eratosthenes(limit)

T = int(input())

for _ in range(T):
    N = int(input())
    count = 0

    for p in range(2, N // 2 + 1):
        if primes[p] and primes[N - p]:
            count += 1
    
    print(count)
