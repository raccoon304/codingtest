import sys 
input = sys.stdin.readline 

n = int(input())
x_li = []
y_li = []

for i in range(0, n, 1):
    x,y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)
    
x = max(x_li) - min(x_li)
y = max(y_li) - min(y_li)    
print( x * y )