import sys
import copy
input = sys.stdin.readline 


while (True):
    x = input().rstrip()
    if x == '0' :
        break 
    else:
        x = list(x)
        re_x = copy.deepcopy(x)
        x.reverse()
        if re_x == x :
            print('yes')
        else:
            print('no')
