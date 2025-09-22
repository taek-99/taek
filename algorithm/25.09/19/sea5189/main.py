import sys
sys.stdin = open('sample_input (17).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n


    def dfs(x, idx, score, visit):
        global min_num

        if idx == n - 1:
            score += board[x][0]
            min_num = min(min_num, score)
            return

        if min_num < score:
            return

        for y in range(n):
            if not visit[y] and x != y:
                visit[y] = True
                dfs(y, idx+1, score+board[x][y], visit)
                visit[y] = False


    min_num = float('inf')
    visited[0] = True
    dfs(0, 0, board[0][0], visited)

    print(f"#{tc} {min_num}")