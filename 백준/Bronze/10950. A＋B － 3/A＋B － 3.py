t = int(input())

def hap(a,b):
    c = a + b 
    return c

for i in range(0, t, 1):
    n,m = map(int, input().split())
    print(hap(n,m))    