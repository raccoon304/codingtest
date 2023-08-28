import sys 
import copy
input = sys.stdin.readline 
li = []

while(1):

    a  = list(map(int, input().split()))
    li = copy.deepcopy(a)
    maxi = max(li)
    li.remove(maxi)
    a = set(a)
    a = list(a)
    if(a[0]!=0):
        if(maxi < li[0] + li[1]):
            if (len(a) == 3):
                print ('Scalene')
            elif (len(a) == 2):
                print ('Isosceles')
            else:
                print ('Equilateral') 
        else:
            print('Invalid')
    else:
        break
