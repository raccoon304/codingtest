import sys 

def plus(a,b):
    print(a+b)

t = int(sys.stdin.readline())
for i in range(0, t, 1):
    a,b = map(int, sys.stdin.readline().split())
    plus(a,b)