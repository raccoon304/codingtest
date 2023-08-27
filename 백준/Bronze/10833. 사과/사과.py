T = int(input())
total = 0
def stock(n,m):
    sto = m % n 
    return sto 

for i in range(0, T, 1):
    n,m = map(int, input().split())
    total += stock(n,m)
    
print(total)