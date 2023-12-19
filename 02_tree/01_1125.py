# 트리의 부모찾기

import sys

def input():
    return sys.stdin.readline().rstrip()

tree = []
N = int(input())
for _ in range(N-1):
    nodes = list(map(int, input().split()))
    tree.append(nodes)

print(tree)
for now_node in range(1, N):
    for i in range(len(tree)):
        if tree[i][1] == now_node:
            print(tree[i][0])