# # 나는야 포켓몬 마스터 이다솜
# import sys

# def input():
#     return sys.stdin.readline().rstrip()

# N, M = map(int, input().split())
# dic = {}
# dic2 = {}
# for i in range(1, N+1):
#     name = input()
#     dic[i] = name
#     dic2[name] = i

# for _ in range(M):
#     inp = input()
#     if inp.isdigit():
#         print(dic[int(inp)])
#     else:
#         print(dic2[inp]) 

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
pocketmon_name = {}
pocketmon_n = {}
for i in range(1, N+1):
    name = input()
    pocketmon_name[name] = i
    pocketmon_n[i] = name
for _ in range(M):
    inp = input()
    if inp.isdigit():
        print(pocketmon_n[int(inp)])
    else:
        print(pocketmon_name[inp])