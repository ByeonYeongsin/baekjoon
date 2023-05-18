# 점프
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
small_rocks = []
jump_counts = {i: [10001, 10001] for i in range(N+1)}
for _ in range(M):
    small_rocks.append(int(input()))

if 2 not in small_rocks:
    jump_counts[2] = [1, 1]
    if 3 not in small_rocks:
        jump_counts[3] = [2, 1]
    if 4 not in small_rocks:
        jump_counts[4] = [2, 2]
for i in range(5, N+1):
    if jump_counts[i] not in small_rocks:
        jump_counts[i] = min(jump_counts[i-now_jump_count]+1, 
                        jump_counts[i-now_jump_count-1]+1,
                        jump_counts[i-now_jump_count+1]+1)
    now_jump_count += 1
if jump_counts[N] < 10001:
    print(jump_counts[N])
else:
    print("-1") 