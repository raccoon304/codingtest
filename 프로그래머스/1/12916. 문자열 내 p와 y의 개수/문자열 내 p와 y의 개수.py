def solution(s):
    str_list = list(s)
    p_chars = ["p","P"]
    y_chars = ["y","Y"]
    p_sum = sum(s.count(chars) for chars in p_chars)
    y_sum = sum(s.count(chars) for chars in y_chars)
    if p_sum == y_sum:
        answer = True
    else:
        answer = False
        
    return answer
