T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    floor_zero = [x for x in range(1, n+1)]
    for _ in range(k):
        for k in range(1, n):
            floor_zero[k] += floor_zero[k-1]
    print(floor_zero[-1])