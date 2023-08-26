import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

s_set = set()
for _ in range(n):
    string = input().rstrip()
    s_set.add(string)

count = 0 

for _ in range(m):
    word = input().rstrip()
    if word in s_set:
        count += 1

print(count)
