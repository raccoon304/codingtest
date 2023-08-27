import sys 
li= []

words = list(map(str, sys.stdin.readline()))
words.pop()

for i in range(97, 123, 1):
    try:
        position = words.index(chr(i)) 
        li.append(position)
    except ValueError:
        li.append(-1)
        
print(" ".join(map(str, li)))