import sys 
input = sys.stdin.readline 

def check_prime(num):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return is_prime

limit = 2 * 123456 
primes = check_prime(limit)

while True:
    M = int(input())
    if M == 0:
        break
    
    count = sum(1 for prime in primes[M+1:2*M+1] if prime)
    print(count)