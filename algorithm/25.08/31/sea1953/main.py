import sys
sys.stdin = open('taek/algorithm/25.08/31/sea1953/sample_input (38).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    next_dir_list = {
        0 : [],
        1 : [0, 1, 2, 3],
        2 : [0, 1],
        3 : [2, 3],
        4 : [1, 2],
        5 : [0, 2],
        6 : [0, 3],
        7 : [1, 3]
    }

    now_dir_list = {
        1 : [0, 1, 2, 3],
        2 : [0, 1],
        3 : [2, 3],
        4 : [0, 3],
        5 : [1, 3],
        6 : [1, 2],
        7 : [0, 2]
    }


    visited[r][c] = True
    new_dq = deque()
    new_dq.append((r, c))
    dq = deque()
    ans = 1
    l -= 1

    while l:
        dq = new_dq
        new_dq = deque()
        while dq:
            x, y = dq.popleft()
            d = board[x][y]
            for ii in now_dir_list[d]:
                nx = x + dx[ii]
                ny = y + dy[ii]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                next_d = board[nx][ny] 
                if ii in next_dir_list[next_d] and not visited[nx][ny]:
                    new_dq.append((nx, ny))
                    visited[nx][ny] = True
                    ans += 1

        l -= 1


    print (f"#{tc} {ans}")
