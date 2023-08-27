Stu = []
total = 0
for i in range(0,5,1):
    Stu.append(int(input()))
    if Stu[i] < 40 :
        total += 40
    else:
        total += Stu[i]
    
print(total//5)
