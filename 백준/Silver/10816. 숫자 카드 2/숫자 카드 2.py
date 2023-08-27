import sys 
input = sys.stdin.readline 

n = int(input())
cards = list(map(int, input().rstrip().split(' ')))
cards.sort()

m = int(input())
targets = list(map(int, input().rstrip().split(' ')))

dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if targets[i] in dic:
        print(dic[targets[i]], end=' ')
    else:
        print(0, end=' ')