# 예산
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
m_list = list(map(int, input().split()))
M = int(input())
m_list.sort(reverse=True)

now_m_list = []
for i in range(1, 100001):
    now_m_list = m_list.copy()
    if sum(m_list) == M:
        break
    else:
        dif, re = divmod(sum(m_list)-M, i)
        if re != 0:
            continue
        for j in range(i):
            now_m_list[j] -= dif
        if now_m_list[i] < now_m_list[i-1]:
            break
print(now_m_list)
