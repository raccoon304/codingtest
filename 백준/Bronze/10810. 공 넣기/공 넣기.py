import sys

n,m = map(int, sys.stdin.readline().split())
li = [0 for l in range(n)]

for e in range( 0, m, 1 ):
    i,j,k = map(int, sys.stdin.readline().split())
    for _ in range( i-1, j, 1 ):
        li[_] = k

print(" ".join(map(str, li)))