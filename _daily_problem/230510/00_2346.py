# 풍선 터뜨리기
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
rot_list = list(map(int, input().split()))
rot_per_bal = {}

for i in range(1, N+1):
    rot_per_bal[i] = rot_list[i-1]

# 1
ballon_lists = [i for i in range(1, N+1)]
ballon_lists = deque(ballon_lists)
now_rot = rot_per_bal[1]
pop_lists = []
pop_lists.append(ballon_lists.popleft())
print(pop_lists)

for _ in range(N-1):
    print(ballon_lists)
    print(now_rot)
    ballon_lists.rotate(-now_rot)
    print(ballon_lists)
    flag = False
    if int(now_rot) > 0: flag=True
    else: falg = False
    print(flag)
    now_rot = rot_per_bal[ballon_lists[-1]]
    if flag:
        pop_lists.append(ballon_lists.pop())
    else:
        pop_lists.append(ballon_lists.popleft())
    print(ballon_lists)

print(pop_lists)
