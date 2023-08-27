import sys 
input = sys.stdin.readline 

n = int(input())
li = []

for i in range(n):
    age, name = input().split()
    li.append((i, int(age), name))

li.sort(key = lambda x : (x[1], x[0]))

for _, age, name in li:  
    print(age, name)