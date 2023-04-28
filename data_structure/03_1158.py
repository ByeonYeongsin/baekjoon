# 요세푸스 문제
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
que = deque([i for i in range(1, N+1)])
que_list = []
while len(que) > 0:
    que.rotate(-(K-1))
    que_list.append(que.popleft())
print('<'+', '.join(map(str, que_list)) + '>')