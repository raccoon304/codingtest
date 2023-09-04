import sys 
input = sys.stdin.readline 

n = int(input())
li = [int(input().rstrip()) for _ in range(n)]
dp = [0] * n

if len(li) <= 2:
    print (sum(li))
    
else:
    dp[0] = li[0]
    dp[1] = li[0] + li[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3] + li[i-1] + li[i], dp[i-2]+li[i] )
    print(dp[-1])