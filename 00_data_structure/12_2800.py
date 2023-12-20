# 2800
# 괄호 제거

import sys

def input():
    return sys.stdin.readline().rstrip()

bracket_id = []
stack = []
bracket_list = []
str = input()
for i in range(len(str)):
    if str[i] == '(':
        bracket_id.append(i)
    elif str[i] == ')':
        last_start_bracket = bracket_id.pop()
        bracket_list.append([last_start_bracket, i])

for now_bracket in bracket_list:
    for i in range(len(str)):
        if i in now_bracket:
            continue
        print(str[i])
    print("\n")

# https://juhee-maeng.tistory.com/91