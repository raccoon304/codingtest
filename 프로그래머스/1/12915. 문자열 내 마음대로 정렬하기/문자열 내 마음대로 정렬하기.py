def solution(strings, n):
    lists = [[string] for string in strings]
    sorted_list = sorted(lists, key=lambda x: (x[0][n], x[0]))
    
    flat_list = [flat for sub in sorted_list for flat in sub]
    answer = flat_list
    
    return answer