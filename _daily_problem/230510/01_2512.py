# 예산
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
m_list = list(map(int, input().split()))
M = int(input())
low = 1
high = M
now_max = (1+M) // 2

while True:
    now_total = 0
    for m in m_list:
        if m < now_max: now_total+= m
        else: now_total += now_max
    if now_total == M:
        break
    elif now_total > M: 
        old_max = now_max
        high = now_max
        now_max = (now_max + low) // 2
        if old_max == now_max:
            break
    else: 
        old_max = now_max
        low = now_max
        now_max = (now_max + high) // 2
        if old_max == now_max:
            break
print(now_max)