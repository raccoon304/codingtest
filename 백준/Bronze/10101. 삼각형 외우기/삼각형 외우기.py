import sys 
input = sys.stdin.readline 

angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

Eq = angle_1 == angle_2 == angle_3
bangak = angle_1 + angle_2 + angle_3

Iso = angle_1 == angle_2 or angle_1 == angle_3 or angle_2 == angle_3

if (Eq == 1):
    print('Equilateral')

else:
    if (bangak==180 and Iso == 1):
        print('Isosceles')
    elif (bangak == 180 and Iso == 0):
        print('Scalene')
    else:
        print("Error")