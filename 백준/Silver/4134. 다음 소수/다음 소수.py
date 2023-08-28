import sys
import math

input = sys.stdin.readline 

def is_prime(x):
    if x <= 1:
        return 'F'
    if x <= 3:
        return 'T'
    if x % 2 == 0 or x % 3 == 0:
        return 'F'
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 'F'
        i += 6
    return 'T'

n = int(input())

for i in range(n):
    a = int(input())
    for j in range (a,a+5000):
        T_F = is_prime(j)
        if T_F == 'T':
            print(j)
            break
        else:
            pass