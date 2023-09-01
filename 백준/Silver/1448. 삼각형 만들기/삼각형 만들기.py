import sys 
input = sys.stdin.readline 

n = int(input())

li = [int(input().rstrip()) for i in range(n)]

li.sort(reverse= True)

count = 0 


while(count < n-2):
    if (li[count] < li[count+1] + li[count+2]):
        print(li[count] + li[count+1] + li[count+2])
        break
    else:
        count+=1

if count == n-2 :
    print(-1)