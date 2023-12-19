# ATM
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
total_p = 0

for i in range(N):
    for j in range(i+1):
        total_p += p_list[j]
print(total_p)