import sys 
input = sys.stdin.readline 

n = int(input())
li = []

for i in range(n):
    command = list(map(str, input().rstrip().split()))
    ct = command[0]
    if ct == 'push':
        li.append(command[1])
    elif ct == 'pop':
        if len(li) >= 1:
            print(li.pop())
        else:
            print(-1)
    elif ct == 'size':
        print(len(li))
    elif ct == 'empty':
        if len(li) == 0 :
            print(1)
        else:
            print(0)
    elif ct == 'top':
        if len(li) >= 1:
            print(li[-1])
        else:
            print(-1)                          