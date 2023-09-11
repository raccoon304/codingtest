from collections import deque
import sys 

T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0 
    while(queue):
        B = max(queue)
        front = queue.popleft()
        M -= 1
        
        if B == front:
            count += 1 
            if M < 0:
                print(count)
                break 
        else:
            queue.append(front)
            if M < 0 :
                M = len(queue) -1 