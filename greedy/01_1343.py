# 폴리오미노
import sys

def input():
    return sys.stdin.readline().rstrip()

str = input()
str_list = str.split('.')
ans = ''

for now_str in str_list:
    if len(now_str) % 2 == 1:
        ans = '-1'
        break
    else:
        while len(now_str) >= 4:
            ans += 'AAAA'
            now_str = now_str[4:]
            str = str[4:]
        if len(now_str) == 2:
            ans += 'BB'
            now_str = now_str[2:]
            str = str[2:]
    while True:
        if len(str) > 0 and str[0] == '.':
            ans += '.'
            str = str[1:]
        else:
            break
print(ans)