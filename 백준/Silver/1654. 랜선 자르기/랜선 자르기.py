import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())

li = [int(input()) for _ in range(N)]
start, end = 1, max(li)

while start <= end:
    mid = (start + end) // 2 
    lines = 0 
    for i in li:
        lines += i // mid 
    if lines >= M:
        start = mid + 1 
    else:
        end = mid - 1 
        
print(end)