T = int(input())

A = T // 300
B = T % 300 // 60
C = T % 300 % 60 // 10
D = T % 300 % 60 % 10

if ( D == 0 ):
    print(A,B,C)
else:
    print('-1')