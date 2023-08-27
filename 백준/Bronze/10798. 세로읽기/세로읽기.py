import sys

li=[]
li = [input() for i in range(5)]

for j in range (0,15,1):
    for i in range(0,5,1):
        if j < len(li[i]):
            print(li[i][j], end='')