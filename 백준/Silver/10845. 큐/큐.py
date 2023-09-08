import sys 
from collections import deque
input = sys.stdin.readline 

n = int(input())
li = deque()

for i in range(n):
    command = list(map(str, input().rstrip().split()))
    ct = command[0]
    if ct == 'push':
        li.append(command[1])
    elif ct == 'pop':
        if len(li) >= 1:
            print(li.popleft())
        else:
            print(-1)
    elif ct == 'size':
        print(len(li))
    elif ct == 'empty':
        if len(li) == 0 :
            print(1)
        else:
            print(0)
    elif ct == 'front':
        if len(li) >= 1:
            print(li[0])
        else:
            print(-1)
    elif ct == 'back':
        if len(li) >= 1:
            print(li[-1])
        else:
            print(-1)
    