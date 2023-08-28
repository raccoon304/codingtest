import sys
num_1, num_2 = map(str, sys.stdin.readline().split())

num_1 = list(num_1)
num_1.reverse()
num_2 = list(num_2)
num_2.reverse()

num1 = "".join(map(str, num_1))
num2 = "".join(map(str, num_2))

if (num1 > num2 ):
    print (num1)
else:
    print(num2)
