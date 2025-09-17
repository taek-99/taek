import sys
sys.stdin = open('input (6).txt','r')

from collections import deque

T = 10

for tc in range(1, T+1):
    n = int(input())
    k = 16
    board = [list(map(int, input())) for _ in range(k)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        for j in range(k):
            if board[i][j] == 2:
                st_x = i
                st_y = j

            if board[i][j] == 3:
                ed_x = i
                ed_y = j

    q = deque()
    q.append((st_x, st_y))

    complete = False
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not board[nx][ny]:
                q.append((nx, ny))
                board[nx][ny] = 1

            if board[nx][ny] == 3:
                complete = True
                break

        if complete:
            break

    print (f"#{tc} {int(complete)}")
