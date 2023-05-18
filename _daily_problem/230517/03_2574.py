# 같은 수로 만들기
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(input()))

count = 0
while True:
    if max(n_list) * len(n_list) == sum(n_list):
        break
    else:
        now_min = min(n_list)
        now_min_index = n_list.index(now_min)
        now_min_left_num = 1000000000
        now_min_right_num = 1000000000
        for i in range(now_min_index-1, -1, -1):
            if n_list[i] == now_min:
                continue
            else:
                now_min_left_num = n_list[i]
                break
        for i in range(now_min_index+1, len(n_list)+1):
            if n_list[i] == now_min:
                continue
            else:
                now_min_right_num = n_list[i]
                break
        
        next_num = min(now_min_left_num, now_min_right_num)

        # n_list[now_min_index] = n_list[now_min_index] + 1
        # for i in range(now_min_index-1, -1, -1):
        #     if n_list[i] == now_min:
        #         n_list[i] = n_list[i] + 1
        #     else:
        #         break
        for i in range(now_min_index, len(n_list) + 1):
            if n_list[i] == now_min:
                n_list[i] = n_list[i] + (next_num-now_min)
            else:
                break
        count += (next_num-now_min)
print(count)