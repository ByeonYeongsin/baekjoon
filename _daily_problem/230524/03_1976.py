# 여행 가자
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
graph = {}
for i in range(1, N+1):
    graph[i] = []

def BFS(root, depart):
    visited[root] = True
    queue = deque([root])
    while queue:
        now_node = queue.popleft()
        if now_node == depart:
            return True
        for next_node in graph[now_node]:
            if next_node != True:
                queue.append(next_node)
                visited[next_node] = True
    return False

for i in range(N):
    now_list = list(map(int, input().split()))
    for j in range(N):
        if now_list[j] == 1:
            graph[i+1].append(j+1)

plan_path = list(map(int, input().split()))
for i in range(M-1):
    visited = [False for _ in range(N+1)]
    if BFS(plan_path[i], plan_path[i+1]) == False:
        print("NO")
        break
else:
    print("YES")
