import sys 
input = sys.stdin.readline

def solution(array):
    count = {}
    for i in array:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_freq = max(count.values())
    modes = [key for key, value in count.items() if value == max_freq]
    if len(modes) > 1:
        return modes
    else:
        return [modes[0]]


N = int(input())
li = [int(input()) for _ in range(N)]

if N > 1 :
    li.sort()
    print(round(sum(li)/N),'\n',li[N//2], sep='')
    li_ch = solution(li)
    if len(li_ch) > 1 :
        print(li_ch[1],'\n',max(li) - min(li), sep='')
    else:
        print(li_ch[0],'\n',max(li) - min(li), sep='')
else:
    print(li[0],'\n',li[0],'\n',li[0],'\n',0, sep='')