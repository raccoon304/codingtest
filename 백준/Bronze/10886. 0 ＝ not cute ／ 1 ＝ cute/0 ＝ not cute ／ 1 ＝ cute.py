judge = []
N = int(input())
for i in range(0, N, 1):
    judge.append(int(input()))
    
NC = judge.count(0)
C = judge.count(1)

if (NC > C):
    print ("Junhee is not cute!")
else:
    print("Junhee is cute!")