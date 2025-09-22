T = int(input())

for tc in range(1, T + 1):
    n, l = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0


    def dfs(idx, score, cal):
        global max_num

        if cal > l:
            return

        if idx == n:
            if cal < l:
                max_num = max(max_num, score)
            return

        dfs(idx + 1, score + nums[idx][0], cal + nums[idx][1])
        dfs(idx + 1, score, cal)


    dfs(0, 0, 0)
    print(f"#{tc} {max_num}")
