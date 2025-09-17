import sys
sys.stdin = open('sample_input (15).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_h = max(max(row) for row in board)
    start_pos = [(i, j) for i in range(n) for j in range(n) if board[i][j] == max_h]


    def dfs(x, y, score, used):
        global max_score

        visited[x][y] = True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not(0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                continue

            if board[x][y] > board[nx][ny]:
                dfs(nx, ny, score + 1, used)
            elif not used:
                for cut in range(1, k+1):
                    if board[x][y] > board[nx][ny] - cut:
                        board[nx][ny] -= cut
                        dfs(nx, ny, score + 1, True)
                        board[nx][ny] += cut

        visited[x][y] = False
        max_score = max(max_score, score)


    max_score = 0
    for i, j in start_pos:
        dfs(i, j, 1, False)

    print(f"#{tc} {max_score}")