# 7662
# 이중 우선순위 큐

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
2
queue = deque()
T = int(input())
for _ in range(T):    
    k = int(input())
    for _ in range(k):
        inp = input().split()
        if inp[0] == 'I':
            if len(queue) == 0:
                queue.append(int(inp[1]))
            else:
                for i in range(len(queue)):
                    if queue[i] < int(inp[1]):
                        continue
                    else:
                        new_queue = deque()
                        for j in range(i):
                            new_queue.append(queue[j])
                        new_queue.append(int(inp[1]))
                        for j in range(i, len(queue)):
                            new_queue.append(queue[j])
                        queue = new_queue
                else:
                    queue.append(int(inp[1]))
        elif inp[0] == 'D': 
            if len(queue) == 0: continue
            else:
                if int(inp[1]) == 1: queue.pop()
                else: queue.popleft()

    if len(queue) == 0: print("EMPTY")
    else: print(queue[-1],' ', queue[0])
            

