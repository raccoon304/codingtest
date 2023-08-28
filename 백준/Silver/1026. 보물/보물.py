import sys
input = sys.stdin.readline 
n = int(input())

A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

A.sort()
B.sort(reverse=True)

total = 0
for i in range(n):
    total += A[i] * B[i]
    
print(total)