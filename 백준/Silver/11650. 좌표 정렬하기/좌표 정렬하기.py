import sys 
input = sys.stdin.readline 

n = int(input())
li = []
li = []

for i in range(n):
    x = list(map(int, input().split()))
    li.append(x)

li = sorted(li, key=lambda x: (x[0], x[1]))

for i in range(n):
    print(li[i][0],li[i][1])