import sys 
input = sys.stdin.readline 

n,m = map(int,input().split())
li = []
count = 0 
cost_li = []
li = [int(input().rstrip()) for i in range(m)]

for i in range(m):
    count = 0
    for j in range(m):
        if (li[j-1] > li[i]):
            count += 1
    count +=1 
    if (count > n):
        count = n
    cost_li.append(count * li[i]) 

x = cost_li.index(max(cost_li))

print (li[x], cost_li[x])