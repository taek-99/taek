import sys
sys.stdin = open('sample_input (12).txt','r')

T = int(input())

for tc in range(1, T+1):
    e, n = map(int, input().split())
    nums = list(map(int, input().split()))

    child = [[] for _ in range(e+1+1)]

    for i in range(0, len(nums), 2):
        idx, val = nums[i], nums[i+1]
        child[idx].append(val)


    def dfs(node):
        global cnt

        if not node:
            return

        for i in node:
            cnt += 1
            if child[i]:
                dfs(child[i])

    cnt = 1
    dfs(child[n])

    print(f"#{tc} {cnt}")