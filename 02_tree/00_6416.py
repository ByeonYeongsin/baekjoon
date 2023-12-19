# 트리인가?
# import sys

# def input():
#     return sys.stdin.readline().rstrip()

# now_tree = []
# max_int = 0
# while True:
#     node1 = int(input())
#     node2 = int(input())
    
#     if node1 == 0 and node2 == 0:
#         root = 0
#         for _ in range(len(now_tree)):
#             print("A")

#     elif node1 == -1 and node2 == -1:
#         break
#     else:
#         now_tree.append([node1, node2])
#         if max_int < node1: max_int = node1
#         if max_int < node2: max_int = node2

import sys

def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.parent = None
    def __str__(self):
        return str(self.data)

def check_solution():
    def check_cycle(root_node):
        cnt = len(root_node.child)
        for 

if __name__ == " __main__":
    is_working = True
    num = 1
    while is_working:
        check = check_solution()
        if not is_working:
            break
        if check:
            string = "Case " + str(num) + " is a tree."
            print(string)
        else :
            string = "Case " + str(num) + " is not a tree."
            print(string)
        num += 1