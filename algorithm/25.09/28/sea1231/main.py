import sys
sys.stdin = open('taek/algorithm/25.09/28/sea1231/input (14).txt','r')


T = 10

for tc in range(1, T+1):
    n = int(input())

    class TreeMake:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key


    tree = [""] * (n+1)
    child = [[] for _ in range(n+1)]

    for idx in range(1, n+1):
        q = list(map(str, input().split()))
        tree[idx] = q[1]

        for i in range(2, len(q)):
            child[idx].append(int(q[i]))

    nodes = [None] * (n+1)

    for i in range(1, n+1):
        nodes[i] = TreeMake(i)


    for i in range(1, n+1):
        kids = child[i]
        if len(kids) >= 1:
            nodes[i].left = nodes[kids[0]]
        if len(kids) >= 2:
            nodes[i].right = nodes[kids[1]]


    def inoder_ans(root):
        global ans
        if root:
            inoder_ans(root.left)
            ans += tree[root.val]
            inoder_ans(root.right)


    root_idx = 1
    ans = ""
    inoder_ans(nodes[root_idx])
    print (f"#{tc} {ans}")