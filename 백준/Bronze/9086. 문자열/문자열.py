import sys 

n = int(sys.stdin.readline())
for i in range(0, n, 1):
    s = list(map(str, sys.stdin.readline()))
    s.pop()
    print(s[0]+s[-1])