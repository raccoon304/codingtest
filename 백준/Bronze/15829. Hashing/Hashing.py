import sys 
input = sys.stdin.readline 

L = int(input())
li = str(input().lstrip().rstrip('\n'))
li = list(li)

ans = 0 

for i in range(L):
    num = (ord(li[i])-96) * (31**i)
    ans += num 

print(ans % 1234567891)

    

