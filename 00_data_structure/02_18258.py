# 18258
# 큐2

# import sys
# from collections import deque

# def input():
#     return sys.stdin.readline().rstrip()

# queue = deque()
# N = int(input())
# for _ in range(N):
#     com = input().split()
#     if com[0] == 'push':
#         queue.append(int(com[1]))
#     elif com[0] == 'pop':
#         print(queue.popleft() if queue else -1)
#     elif com[0] == 'size':
#         print(len(queue))
#     elif com[0] == 'empty':
#         print(0 if queue else 1)
#     elif com[0] == 'front':
#         print(queue[0] if queue else -1)
#     elif com[0] == 'back':
#         print(queue[-1] if queue else -1)

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0: print("1")
        else: print("0")
    elif cmd[0] == 'front':
        if len(queue) == 0: print("-1")
        else: print(queue[0])
    elif cmd[0] == 'back':
        if len(queue) == 0: print("-1")
        else: print(queue[-1])