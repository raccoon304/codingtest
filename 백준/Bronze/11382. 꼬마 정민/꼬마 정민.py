import sys

def hap(a,b,c):
    total = a + b + c
    return total
A,B,C = map(int,sys.stdin.readline().split())

print(hap(A,B,C))