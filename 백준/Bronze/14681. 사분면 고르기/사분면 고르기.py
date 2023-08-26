import sys 

def quadrant(a,b):
    if (a > 0 and b > 0):
        print('1')
    elif ( a > 0 and b < 0):
        print('4')
    elif ( a < 0 and b > 0):
        print('2')
    elif ( a < 0 and b < 0):
        print('3')

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

quadrant(x,y)