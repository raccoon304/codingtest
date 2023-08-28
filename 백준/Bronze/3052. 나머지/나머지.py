import sys

t = 0
f = 0

ans = []
for i in range(1,11,1):
    n = int(sys.stdin.readline())
    nam = n % 42
    ans.append(nam)
    
a = set(ans)
ans = list(a)

print(len(ans))