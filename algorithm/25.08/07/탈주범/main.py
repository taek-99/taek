from collections import deque
import sys
sys.stdin = open('sample_input (17).txt','r')

T = int(input())

for tc in range (1, T+1):
    n, m, rx, ry, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range (n)]
    visited = [[False] * m for _ in range (n)]


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dz = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
    pipe_dict = {
            1 : (0, 1, 2, 3),
            2 : (0, 1),
            3 : (2, 3),
            4 : (0, 3),
            5 : (1, 3),
            6 : (1, 2),
            7 : (0, 2)
    }

    ans = 1
    dq = deque()
    move_dq = deque()
    dq.append((rx, ry))
    visited[rx][ry] = True

    for i in range (l-1, 0, -1):
        while dq:
            (x, y) = dq.popleft()
            for ii in pipe_dict[board[x][y]]:
                nx = x + dx[ii]
                ny = y + dy[ii]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if board[nx][ny] in dz[ii]:
                        ans += 1
                        visited[nx][ny] = True
                        move_dq.append((nx, ny))

        dq = move_dq
        move_dq = deque()

    print (f"#{tc} {ans}")



