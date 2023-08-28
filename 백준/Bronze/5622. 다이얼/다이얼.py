import sys

time_count = 0
alpha = list(sys.stdin.readline().rstrip())
a = []

 
for i in range ( 0, len(alpha), 1):
    a.append(ord(alpha[i]))
    if (a[i] >= 65 and a[i] <= 67 ):
        time_count += 3
    elif( a[i] >= 68 and a[i] <=70 ):
        time_count += 4
    elif( a[i] >= 71 and a[i] <=73 ):
        time_count += 5
    elif( a[i] >= 74 and a[i] <=76 ):
        time_count += 6
    elif( a[i] >= 77 and a[i] <=79 ):
        time_count += 7
    elif( a[i] >= 80 and a[i] <=83 ):
        time_count += 8
    elif( a[i] >= 84 and a[i] <=86 ):
        time_count += 9
    elif( a[i] >= 87 and a[i] <=90 ):
        time_count += 10
    
print (time_count)