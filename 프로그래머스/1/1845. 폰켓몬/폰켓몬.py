def solution(nums):
    a1 = int(len(nums)/2)
    r1 = set(nums)
    r2 = list(r1)
    a2 = len(r2)
    if a2 >= a1 :
        answer = a1
    else:
        answer = a2
    return answer