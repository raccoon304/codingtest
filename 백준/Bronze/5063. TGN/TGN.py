T = int(input())
for i in range(0, T, 1):
    r,e,c = map(int,input().split())
    if ( r - (e - c) > 0 ):
        print('do not advertise')
    elif ( r - (e - c) == 0):
        print('does not matter')
    else:
        print('advertise')