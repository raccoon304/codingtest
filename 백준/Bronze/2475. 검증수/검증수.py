import sys 
input = sys.stdin.readline 

li = list(map(int, input().split()))

for _ in range(5):
    li[_] = li[_]**2

print(sum(li)%10) 