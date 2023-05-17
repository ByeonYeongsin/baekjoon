# 트리의 부로 찾기
# 완

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(visited, graph, root, parents):
    queue = deque([root])
    visited[root] = True
    while queue:
        n = queue.popleft()
        for node in graph[n]:
            if visited[node] != True:
                if parents[node] == 0:
                    parents[node] = n
                queue.append(node)
                visited[node] = True
    return parents

N = int(input())
graph = {}
for i in range(N+1):
    graph[i] = []
visited = [False for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
result = BFS(visited, graph, 1, parents)
for i in range(2, len(result)):
    print(result[i])
