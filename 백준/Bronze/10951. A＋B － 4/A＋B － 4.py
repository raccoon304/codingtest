import sys 

def plus(a,b):
    print(a+b)

while True:
    try:     
        a,b = map(int, sys.stdin.readline().split())
        plus(a,b)
    except:
        break