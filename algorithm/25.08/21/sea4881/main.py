import sys
sys.stdin = open('sample_input (2).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    col_list = [0] * n
    min_ans = float("INF")


    def dfs(cnt, ans, col):
        global min_ans

        if cnt == n:
            min_ans = min(min_ans, ans)
            return

        if ans > min_ans:
            return

        for i in range(n):
            if col[i] < 1:
                col[i] += 1
                dfs(cnt+1, ans+board[cnt][i], col)
                col[i] -= 1


    dfs(0, 0, col_list)

    print(f"#{tc} {min_ans}")