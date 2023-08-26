import sys 
input = sys.stdin.readline 

stack = [] 

N = int(input())

for i in range(N):
    num = list(map(int, input().rstrip().split()))

    if (num[0] == 1):
        stack.append(num[1])
    elif (num[0] == 2):
        if (len(stack) >= 1):
            print(stack.pop())
        else:
            print ('-1')
    elif (num[0] == 3):
        print(len(stack))
    elif (num[0] == 4):
        if (len(stack)==0):
            print('1')
        else:
            print('0')
    elif (num[0] == 5):
        if (len(stack) >= 1):
            print(stack[-1])
        else:
            print('-1')
        