T = int(input())
ans = []
for i in range(0,T,1):
    A,B= map(int, input().split())
    C = A+B
    ans.insert(i,C) 
        
for x in range(0,len(ans),1):
    print('Case #%d:'%(x+1),ans[x])