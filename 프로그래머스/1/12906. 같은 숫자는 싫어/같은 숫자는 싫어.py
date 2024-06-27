def solution(arr):
    ans = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            ans.append(arr[i])
    return ans