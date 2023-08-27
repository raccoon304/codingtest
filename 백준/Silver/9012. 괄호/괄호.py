import sys 
input = sys.stdin.readline 

T = int(input())

for i in range(T):
    stack = []
    x = input().rstrip()
    for j in x :
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break 
            
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
    