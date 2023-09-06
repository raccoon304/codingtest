import sys
from collections import deque 
input = sys.stdin.readline 

def dfs(graph, start_node):
    queue = deque([start_node])
    visit = []
    
    while queue:
        node = queue.pop()
        if node not in visit:
            visit.append(node)
            if node not in graph:
                return visit
            queue.extend(graph[node])
    return visit 

def bfs(graph, start_node):
    queue = deque([start_node])
    visit = []    
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node not in graph:
                return visit 
            queue.extend(graph[node])
    return visit 

N,M,V = map(int, input().split())
graph = {}

for _ in range(M):
    key, value = map(int,input().split())
    if key not in graph:
        graph[key] = []
    if value not in graph:
        graph[value] = [] 
    graph[key].append(value)
    graph[value].append(key)
    
for key in graph:
    graph[key].sort(reverse = True)
print(*dfs(graph, V))

for key in graph:
    graph[key].sort()
print(*bfs(graph, V))