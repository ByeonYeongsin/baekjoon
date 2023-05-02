# 카드2
import sys

def input():
    return sys.stdin.readline().rstrip()
tree_dic = {}
count = 0

while True:
    now_str = input()
    if now_str == '':
        break
    if now_str in tree_dic:
        count += 1
        tree_dic[now_str] = tree_dic[now_str] + 1
    else:
        tree_dic[now_str] = 1
        count += 1

sorted(tree_dic.keys())
for key in tree_dic.keys():
    print(key, round(tree_dic[key]/count))
