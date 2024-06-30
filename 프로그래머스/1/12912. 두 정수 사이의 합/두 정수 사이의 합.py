def solution(a, b):
    hap = 0
    start = min(a,b)
    end = max(a,b)
    for i in range(start,end+1,1):
        hap += i
    answer = hap
    return answer
