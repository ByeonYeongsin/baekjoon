# 진법 변환
import sys

def input():
    return sys.stdin.readline().rstrip()

B, N = input().split()
n10 = 0
now = 1
B = B[::-1]

for i in B:
    if i >= 'A' and i <= 'Z':
        i = i - 'A' + 10
    if i >= '0' and i <= '9':
        i = int(i)
    n10 = n10 + now * i
    now = now * N

print(n10)