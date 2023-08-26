import sys

total_cost = 0

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
for i in range(0, n, 1):
    cost, count = map(int, sys.stdin.readline().split())
    total_cost += (cost * count)
    
if( total_cost == x ):
    print('Yes')
else:
    print('No')