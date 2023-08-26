def hap(a,b):
    c = a + b 
    return c

while(1):
    n,m = map(int, input().split())
    if(n==0 and m==0):
        break
    else:
        print(hap(n,m))
    