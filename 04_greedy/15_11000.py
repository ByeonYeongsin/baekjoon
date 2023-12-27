# 11000
# 강의실 배정
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []
class_time = []
for _ in range(N):
    si, ti = map(int, input().split())
    class_time.append([si, ti])
class_time.sort()
heapq.heappush(heap, class_time[0][1])

for i in range(1, N):
    if class_time[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, class_time[i][1])
    else:
        heapq.heappush(heap, class_time[i][1])
print(len(heap))