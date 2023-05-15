# 트리인가?
import sys

def input():
    return sys.stdin.readline().rstrip()

now_tree = []
max_int = 0
while True:
    node1 = int(input())
    node2 = int(input())
    
    if node1 == 0 and node2 == 0:
        root = 0
        for _ in range(len(now_tree)):
            print("A")

    elif node1 == -1 and node2 == -1:
        break
    else:
        now_tree.append([node1, node2])
        if max_int < node1: max_int = node1
        if max_int < node2: max_int = node2