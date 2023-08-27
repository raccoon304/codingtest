import sys 
input = sys.stdin.readline 

words = []


while(True): 
    x = input().rstrip()

    if x[0] == '.':
        break
    else:
        words.append(list(x))
        
        
for i in words:
    stack = []
    for j in i:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                if stack.pop() != '(':
                    print('no')
                    break
            else:
                print('no')
                break
        elif j == '[':
            stack.append(j)
        elif j == ']':
            if stack:
                if stack.pop() != '[':
                    print('no')
                    break
            else:
                print('no')
                break 
            
            
    else:
        if not stack:
            print ('yes')
        else:
            print('no')
    
        