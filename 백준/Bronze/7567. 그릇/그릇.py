B = input()
A = list(B) 
height = 10

for i in range(0,len(A)-1,1):
    if (A[i] == A[1+i]):
        height += 5
    else:
        height += 10
        
print(height)