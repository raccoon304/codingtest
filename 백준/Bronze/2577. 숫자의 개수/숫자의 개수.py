A = int(input()) 
B = int(input())
C = int(input())

D = A*B*C
li = list(str(D))
li = list(map(int,li))

for i in range(10):
    print(li.count(i))