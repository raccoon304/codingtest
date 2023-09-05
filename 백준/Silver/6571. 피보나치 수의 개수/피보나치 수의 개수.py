import sys 
input = sys.stdin.readline 

dp = [0] * 1001
dp[1] = 1 
dp[2] = 2

for i in range(3,1001,1):
    dp[i] = dp[i-1] +dp[i-2]

while(1):
    a,b = map(int, input().split())
    count = 0
    if a == 0 and b == 0 :
        break
    for i in range( 1,1001,1):
        if a <= dp[i] and dp[i] <= b:
            count += 1 
    print(count)
    
    