import sys 
input = sys.stdin.readline 

n = int(input())
se = set(map(int, input().rstrip().split()))
m = int(input())
li = list(map(int, input().rstrip().split()))

for num in li:				
    print(1) if num in se else print(0)