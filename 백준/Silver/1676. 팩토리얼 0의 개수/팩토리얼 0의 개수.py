import sys 
from math import factorial
input = sys.stdin.readline
li = list(str(factorial(int(input()))))

count = 0

while (True):
    if li[-1] == '0':
        count += 1
        li.pop()
    else:
        break 
    
print(count)

