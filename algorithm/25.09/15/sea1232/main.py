import sys
sys.stdin = open('input (4).txt','r')

T = 10

for tc in range(1, T+1):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    node = [[] for _ in range(n+1)]

    for _ in range(n):
        nums = list(map(str, input().split()))

        idx = int(nums[0])

        try:
            a = int(nums[1])
        except ValueError:
            tree[idx] = nums[1]
            node[idx].append(int(nums[2]))
            node[idx].append(int(nums[3]))
            continue
        else:
            tree[idx] = int(nums[1])


    def dfs(x):
        if type(tree[x]) == int:
            return tree[x]

        if tree[x] == '+':
            return dfs(node[x][0]) + dfs(node[x][1])

        if tree[x] == '-':
            return dfs(node[x][0]) - dfs(node[x][1])

        if tree[x] == '*':
            return dfs(node[x][0]) * dfs(node[x][1])

        if tree[x] == '/':
            return int(dfs(node[x][0]) / dfs(node[x][1]))


    ans = dfs(1)

    print(f"#{tc} {ans}")

