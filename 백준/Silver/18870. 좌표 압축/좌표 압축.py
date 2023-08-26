import sys 
input = sys.stdin.readline 


m = int(input())
n = list(map(int, input().rstrip().split()))

li = set(n)
li = list(li)
li.sort()

diction = {}
for i in range(len(li)):
    diction[li[i]] = i
for i in n:
    print(diction[i], end=' ')