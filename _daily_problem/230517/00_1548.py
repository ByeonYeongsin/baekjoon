# # 부분 삼각 수열
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
len_list = list(map(int, input().split()))
len_list.sort()
# print(len_list)

for start in range(N,):
    if len(len_list) == 1:
        print("1")
        break
    if len(len_list) == 2:
        print("2")
        break
    if len_list[start] + len_list[start+1] <= len_list[-1]:
        if len_list[-1] - len_list[len(len_list)//2] > len_list[len(len_list)//2] - len_list[0]:
            len_list = len_list[:-1]
        else:
            len_list = len_list[1:]
    else:
        print(len(len_list))
        break

