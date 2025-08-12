import sys
sys.stdin = open('sample_input(1) (2).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(m)]
    board = [[0] * (n+1) for _ in range(n+1)]

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    a = (n // 2) + 1
    b = n // 2
    board[b][b] = 2
    board[b][a] = 1
    board[a][b] = 1
    board[a][a] = 2

    def sol(x, y, color):
        for ii in range(8):
            for jj in range(1, n):
                nx = x + (dx[ii] * jj)
                ny = y + (dy[ii] * jj)
                if 0 <= nx < n+1 and 0 <= ny < n+1:
                    if board[nx][ny] == 0:
                        break
                    if board[nx][ny] == color:
                        for k in range(jj - 1, 0, -1):
                            nnx = x + (dx[ii] * k)
                            nny = y + (dy[ii] * k)
                            board[nnx][nny] = color
                        break


    for y, x, color in nums:
        board[x][y] = color
        sol(x, y, color)

    b_cnt = 0
    w_cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1

    print(f"#{tc} {b_cnt} {w_cnt}")