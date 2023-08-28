n = int(input())
cla = []
for i in range(n):
    student = input().split()
    student[1] = int(student[1])  
    student[2] = int(student[2])  
    student[3] = int(student[3])  
    cla.append(student)

cla.sort(key=lambda x: (x[3], x[2], x[1]))  
print(cla[-1][0])
print(cla[-0][0])