import sys 

li = []
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
ans = int(sys.stdin.readline())
print(li.count(ans))