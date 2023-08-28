T = int(input())

ox_l = []

for i in range(0,T,1):
    ox = input()
    ox_l = list(ox)
    score = 0
    o_score =0
    for i in range(0,len(ox_l),1):
        a = ox_l.pop()
        if (a == 'O'):
            o_score += 1
            score += o_score
        if ( a == 'X'):
            o_score = 0
    print(score)         