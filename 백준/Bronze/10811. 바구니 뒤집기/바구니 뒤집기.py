import sys

n,m = map(int, sys.stdin.readline().split())
li = [_ for _ in range(1,n+1,1)]

for i in range(0, m, 1):
    a,b = map(int, sys.stdin.readline().split())
    sublist = li[a-1:b]
    sublist.reverse()
    li[a-1:b] = sublist

print(" ".join(map(str, li)))