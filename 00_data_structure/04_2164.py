# 카드2
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
que = deque([i for i in range(1, N+1)])
while len(que) > 1:
    que.popleft()
    que.rotate(-1)

print(que[0])