li = list(map(int, input().split()))

count = 0
des_count = 8
asc_count = 1
ans = 0 
 
while(count < 8): 
    if li[count] == des_count:
        ans -= 1
    elif li[count] == asc_count:
        ans += 1 
    else:
        pass 
    count += 1
    des_count -= 1
    asc_count += 1  
    
if ans == 8:
    print('ascending')
elif ans == -8:
    print('descending')
else:
    print('mixed')    

    
