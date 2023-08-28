T = int(input())

for i in range(T):
    A = list(map(str, input().split()))
    ans = 0
    for j in range(len(A)):
        if j == 0:
            ans +=float(A[j])
        else:
            if A[j] == "#":
                ans  -= 7
            elif A[j]  == "%":
                ans += 5
            elif A[j] == "@":
                ans *= 3
    print("%0.2f" %ans)                

        