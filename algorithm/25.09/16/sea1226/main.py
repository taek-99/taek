import sys
sys.stdin = open('input (4).txt','r')

T = 10

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                st_x, st_y = i, j

            if board[i][j] == 3:
                ed_x, ed_y = i, j


    def dfs(x, y):
        global complete

        if (x, y) == (ed_x, ed_y):
            complete = 1

        if complete:
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if board[nx][ny] == 1 or board == 2:
                continue

            board[nx][ny] = 1
            dfs(nx, ny)
            board[nx][ny] = 0


    complete = 0
    dfs(st_x, st_y)
    print(f"#{n} {complete}")