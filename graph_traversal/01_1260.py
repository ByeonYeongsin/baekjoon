# DFS와 BFS
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(visited, graph, root):
    visited[root] = True
    queue = deque([root])
    path = []
    while queue:
        n = queue.popleft()
        path.append(n)
        for node in graph[n]:
            if visited[node] != True:
                queue.append(node)
                visited[node] = True
    return path

def DFS(visited, graph, root):
    visited[root] = True
    stack = [root]
    path = []
    while stack:
        n = stack.pop()
        path.append(n)
        for node in graph[n]:
            if visited[node] != True:
                stack.append(node)
                visited[node] = True
    return path

N, M, V = map(int, input().split())
visited = [False for _ in range(N+1)]
graph = {}
for i in range(N+1):
    graph[i] = []

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
print(DFS(visited, graph, V))
visited = [False for _ in range(N+1)]
print(BFS(visited, graph, V))