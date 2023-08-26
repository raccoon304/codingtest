T = int(input())

for i in range(0, T, 1):
    j = int(input())
    C_total = 0
    G_total = 0
    for j in range(0, j, 1):
        C, G = map(float, input().split())
        C_total += C
        G_total += C * G
    G_total /= C_total
    print(int(C_total), '%.1f'%G_total)
