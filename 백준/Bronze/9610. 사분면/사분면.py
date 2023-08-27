T = int(input())
axis = 0
Q = [0,0,0,0]

for i in range(0,T,1):
    A,B = map (int, input().split())
    if (A == 0 or B == 0):
        axis += 1 
    elif ( A > 0 and B > 0  ):
        Q[0] += 1
    elif ( A < 0 and B > 0 ):
        Q[1] += 1
    elif ( A > 0 and B < 0 ):
        Q[3] += 1
    elif ( A < 0 and B < 0 ):
        Q[2] += 1
        
for i in range (0,4,1):
    n = i +1 
    s = Q[i]
    print(f'Q{n}: {s}')
print(f'AXIS: {axis}')
