n = int(input())

C_score = 100
J_score = 100

for i in range(0, n, 1):
    chang, jung = map(int, input().split())
    if (chang > jung):
        J_score -= chang
    elif ( jung > chang ):
        C_score -= jung
    else:
        pass 

print(C_score)
print(J_score)