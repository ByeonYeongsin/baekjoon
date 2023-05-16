# 노드 사이의 거리
import sys
from collections import deque

def BFS(tree, visited, t1, t2):
    path = []
    queue = deque([t1])
    visited[t1] = True

    while queue:
        v = queue.popleft()
        path.append(v)
        if v == t2:
            break
        else:
            for i in tree[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    return path

def input():
    return sys.stdin.readline().strip()

N, M = map(int, input().split())
tree = {}
for i in range(N+1):
    tree[i] = []

dis_list = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N-1):
    t1, t2, dis = map(int, input().split())
    tree[t1].append(t2)
    tree[t2].append(t1)
    dis_list[t1][t2] = dis
    dis_list[t2][t1] = dis

for _ in range(M):
    t1, t2 = map(int, input().split())
    visited = [False] * (N+1)
    path = BFS(tree, visited, t1, t2)
    distance = 0
    for i in range(len(path)-1):
        distance += dis_list[path[i]][path[i+1]]
    print(distance)
    