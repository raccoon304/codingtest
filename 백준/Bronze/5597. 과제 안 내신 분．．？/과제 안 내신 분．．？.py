import sys

li =[]
for _ in range(1,31,1):
    li.append(_)

for i in range(0,28,1):
    student = int(sys.stdin.readline())
    li.remove(student)
    
li.sort()
print(li[0])
print(li[1])
