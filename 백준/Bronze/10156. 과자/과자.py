K,N,M = map(int,input().split())
need_money = K * N - M 
if (need_money < 0):
    need_money = 0
else:
    pass
print(need_money) 