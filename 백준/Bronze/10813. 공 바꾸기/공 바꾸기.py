import sys

n,m = map(int, sys.stdin.readline().split())
li = []


    
for i in range( 1, n+1, 1):
    li.append(i)
    
for _ in range( 0, m, 1):
    a,b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    temp = 0
    temp = li[a]
    li[a] = li[b]
    li[b] = temp

print(" ".join(map(str, li)))