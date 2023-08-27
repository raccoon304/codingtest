import sys
li = []
ans = []
n, x = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

for i in range(0, n, 1):
    if(li[i] < x ):
        ans.append(li[i])

print(" ".join(map(str, ans)))