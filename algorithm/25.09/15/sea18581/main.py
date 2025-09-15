import sys
sys.stdin = open('input (3).txt','r')

n = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(n+1)]


for i in range(0, len(nums), 2):
    idx = nums[i]
    val = nums[i+1]
    tree[idx].append(val)

root_idx = 1


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


nodes = [None] + [TreeNode(i) for i in range(1, n+1)]


for idx in range(1, n+1):
    kids = tree[idx]
    if len(kids) >= 1:  # 왼쪽
        nodes[idx].left = nodes[kids[0]]
    if len(kids) == 2:  # 오른쪽
        nodes[idx].right = nodes[kids[1]]


def pre_ans(root):  # 전위
    if root:
        print(root.val, end=' ')
        pre_ans(root.left)
        pre_ans(root.right)


def cen_ans(root):  # 중위
    if root:
        cen_ans(root.left)
        print(root.val, end=' ')
        cen_ans(root.right)


def pos_ans(root):  # 후위
    if root:
        pos_ans(root.left)
        pos_ans(root.right)
        print(root.val, end=' ')


root = nodes[1]

pre_ans(root)
print()
cen_ans(root)
print()
pos_ans(root)
print()