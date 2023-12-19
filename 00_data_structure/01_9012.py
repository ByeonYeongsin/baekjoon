# # 9012
# import sys

# def input():
#     return sys.stdin.readline().rstrip()

# N = int(input())
# for _ in range(N):
#     string = input()
#     stack = []
#     for s in string:
#         if s == '(':
#             stack.append(0)
#         elif s == ')':
#             if len(stack) == 0:
#                 print("NO")
#                 break
#             stack.pop(0)
#     else:
#         if len(stack) == 0:
#             print("YES")
#         else:
#             print("NO")

import sys

def input():
    return sys.stdin.readline()

T = int(input())
for _ in range(T):
    flag = True
    line = input()
    stack = []
    for s in line:
        if s == '(':
            stack.append(0)
        elif s == ')':
            if len(stack) == 0:
                flag = False
                break
            stack.pop()
    if len(stack) != 0: flag = False

    if flag == True: print("YES")
    else: print("NO")
