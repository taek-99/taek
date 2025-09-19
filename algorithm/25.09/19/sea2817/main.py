import sys
sys.stdin = open('sample_input (16).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    visited = [False] * n


    def dfs(idx, score):
        global ans

        if idx == n:
            return

        if score == k:
            ans += 1
            return

        if score > k:
            return

        for i in range(idx, n):

            if not visited[i]:
                visited[i] = True
                dfs(i, score+nums[i])
                visited[i] = False


    ans = 0
    dfs(0, 0)
    print(f"#{tc} {ans}")