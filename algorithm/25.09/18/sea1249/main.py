import sys
sys.stdin = open('input (5).txt','r')

import heapq

T = int(input())

for tc in range(1,  T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    num_board = [[float('inf')] * n for _ in range(n)]

    st_x = st_y = 0
    ed_x = ed_y = n-1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    hq_board = [(0, 0, 0)]

    while hq_board:
        val, x, y = heapq.heappop((hq_board))

        if val > num_board[x][y]:
            continue

        if x == ed_x and y == ed_y:
            print(f'#{tc} {val}')

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                nt = val + board[nx][ny]
                if nt < num_board[nx][ny]:
                    num_board[nx][ny] = nt
                    heapq.heappush(hq_board, (nt, nx, ny))

