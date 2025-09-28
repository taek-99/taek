import sys
sys.stdin = open('taek/algorithm/25.09/28/sea1231/input (14).txt','r')

T = 10

for tc in range(1, T+1):
    n = int(input())
    tree = [""] * (n+1)
    child = [[] for _ in range(n+1)]

    for _ in range(n):
        q = list(map(str, input().split()))
        idx = int(q[0])
        tree[idx] = q[1]

        for i in range(2, len(q)):
            child[idx].append(int(q[i]))

    class TreeMake:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key


    nodes = [None] * (n+1)
    for i in range(1, n+1):
        nodes[i] = TreeMake(i)

    for i in range(1, n+1):
        key = child[i]

        if len(key) >= 1:
            nodes[i].left = nodes[key[0]]
        if len(key) >= 2:
            nodes[i].right = nodes[key[1]]

    def in_order(root):
        global ans

        if root:
            in_order(root.left)
            ans += tree[root.val]
            in_order(root.right)

    start_idx = 1
    ans = ""
    in_order(nodes[start_idx])
    print (f"#{tc} {ans}")