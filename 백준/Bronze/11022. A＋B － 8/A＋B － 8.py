T = int(input())
ans = []
Al =[]
Bl =[]
for i in range(0,T,1):
    A,B= map(int, input().split())
    C = A+B
    ans.insert(i,C)
    Al.insert(i,A)
    Bl.insert(i,B)
        
for x in range(0,len(ans),1):
    print('Case #%d:'%(x+1),Al[x],'+',Bl[x],'=',ans[x])