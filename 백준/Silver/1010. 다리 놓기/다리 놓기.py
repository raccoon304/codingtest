from math import factorial
import sys 
input = sys.stdin.readline 

T = int(input())
for i in range(T):
    n,m = map(int, input().split())
    x = factorial(m) // (factorial(n)*factorial(m-n))
    print(x)