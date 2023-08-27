T = int(input())
for i in range (0, T, 1):        
    Y_score = 0
    K_score = 0
    for i in range (0, 9, 1):
        Y, K = map(int, input().split())
        Y_score += Y
        K_score += K
    if (Y_score > K_score):
        print ('Yonsei')
    elif ( K_score > Y_score):
        print ('Korea')
    else:
        print('Draw')