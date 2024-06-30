def solution(n):
    count = 0
    primes = [False, False] + [True] * (n-1)
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i] == True:
            for j in range(i*2, n+1, i):
                primes[j] = False

    return primes.count(True)
