import sys 
input = sys.stdin.readline 

n = int(input())
li = [0] * 1001

li[0] = 1
li[1] = 1

for i in range(2,1001):
    li[i] = (li[i-1] + li[i-2] + li[i-2]) % 10007
    
print(li[n])