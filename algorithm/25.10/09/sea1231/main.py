import sys
sys.stdin = open('taek/algorithm/25.10/09/sea1231/input (15).txt','r')

T = 10

for tc in range(1, T+1):
    n = int(input())
    node = [""] * (n+1)
    tree = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        data = list(map(str, input().split()))
        node[i] = data[1]
        
        for idx in range(2, len(data)):
            tree[i].append(int(data[idx]))

    class MakeTree:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.key = val

    nodes = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        nodes[i] = MakeTree(node[i])

    for i in range(1, n+1):
        idx = tree[i]
        if len(idx) >= 1:
            nodes[i].left = nodes[idx[0]]
        if len(idx) >= 2:
            nodes[i].right = nodes[idx[1]]


    def in_order(arr):
        global ans

        if arr.left:
            in_order(arr.left)
        ans += arr.key
        if arr.right:
            in_order(arr.right)


    ans = ""
    in_order(nodes[1])

    print (f"#{tc} {ans}")