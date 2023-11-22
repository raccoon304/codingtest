T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    Y = (N // H) + 1
    X = N % H  
    if X == 0:
        X = H
        Y -= 1
    print(X*100+Y)