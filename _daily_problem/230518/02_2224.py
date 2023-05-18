# 명제 증명

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(visited, graph, root):
    queue = deque([root])
    visited[root] = True
    nodes = []
    while queue:
        node = queue.popleft()
        nodes.append(node)
        for next_node in graph[node]:
            if visited[next_node] == False:
                queue.append(next_node)
                visited[next_node] = True
    return nodes 

graph = {}
X = int(input())
for _ in range(X):
    x, y = input().split(' => ')
    if x in graph:
        graph[x].append(y)
        if y not in graph:
            graph[y] = []
    else:
        graph[x] = [y]
        if y not in graph:
            graph[y] = []
    
sorted(graph)
for root in graph.keys():
    visited = {}
    for key in graph.keys():
        visited[key] = False
    for values in graph.values():
        for value in values:
            visited[value] = False
    nodes = BFS(visited, graph, root)
    nodes = sorted(nodes[1:])
    for now_node in nodes:
        print(root, ' => ', now_node)