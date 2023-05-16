# 바이러스

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(visited, graph, root):
    queue = deque([root])
    visited[root] = True
    paths = []

    while queue:
        n = queue.pop()
        paths.append(n)
        for node in graph[n]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
    
    return paths

n_computers = int(input())
graph = {}
for i in range(n_computers+1):
    graph[i] = []
visited = [False for _ in range(n_computers+1)]
n_pairs = int(input())

for _ in range(n_pairs):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
path = BFS(visited, graph, 1)

print(len(path)-1)