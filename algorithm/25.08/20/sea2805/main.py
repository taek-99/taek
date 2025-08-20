import sys
sys.stdin = open('input (27).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(n):
        bd = list(map(str, input()))
        board.append(bd)

    visited = [[False] * n for _ in range(n)]
    k = (n // 2)
    ans = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append((k, k))
    visited[k][k] = True
    ans += int(board[k][k])

    for _ in range(1, k+1):
        new_dq = deque()
        while dq:
            (x, y) = dq.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    new_dq.append((nx, ny))
                    visited[nx][ny] = True
                    ans += int(board[nx][ny])
        dq = new_dq
    print (f"#{tc} {ans}")
