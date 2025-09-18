import sys
sys.stdin = open('input (4).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    bomb = [[0]*n for _ in range(n)]

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                bomb[i][j] = -999
                visited[i][j] = True
                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if not (0 <= nx < n and 0 <= ny < n) or bomb[nx][ny] < 0:
                        continue

                    bomb[nx][ny] += 1


    def dfs(x, y):
        visited[x][y] = True

        if bomb[x][y] != 0:
            return

        bomb[x][y] = -999

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0 <= nx < n and 0 <= ny < n):
                continue

            if bomb[nx][ny] >= 0:
                dfs(nx, ny)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == 0:
                cnt += 1
                dfs(i, j)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1

    print(f"#{tc} {cnt}")