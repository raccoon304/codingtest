import sys 

total = 0
n = int(sys.stdin.readline())
number = list(map(str, sys.stdin.readline()))
number.pop()

for i in range(0, n, 1):
    total += int(number[i])     

print(total)