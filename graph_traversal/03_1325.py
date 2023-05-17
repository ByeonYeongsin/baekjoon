# 효율적인 해킹
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def BFS(graph, visited, root):
    queue = deque([root])
    visited[root] = True
    len = 1
    while queue:
        n = queue.popleft()
        len += 1
        for node in graph[n]:
            if visited[node] != True:
                queue.append(node)
                visited[node] = True
    return len

N, M = map(int, input().split())
reli_list = []
graph = {}

for i in range(N+1):
    graph[i] = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_len = 0
max_len_list = []
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    now_len = BFS(graph, visited, i)
    if now_len > max_len:
        max_len_list = [i]
        max_len = now_len
    elif now_len == max_len:
        max_len_list.append(i)
print(max_len_list.sort())