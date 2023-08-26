import copy

T = int(input())
for _ in range(0, T, 1):
    case = int(input())
    name_l = []
    L_l = []
    judang = []
    L_sort=[]
    temp = 0
    for i in range(0, case, 1):
        L, name = map(str,input().split())
        name_l.append(name)
        L_l.append(int(L))
    L_sort = copy.deepcopy(L_l)
    L_sort.sort()
    temp = L_sort[-1]
    best_n = L_l.index(temp)
    JOY = name_l[best_n]
    
    print(JOY)