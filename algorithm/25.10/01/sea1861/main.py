import sys
sys.stdin = open('input (10).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def bfs(r, c):
        q = deque()
        visited = set()
        q.append((r, c))
        visited.add((r, c))
        cnt = 1

        while q:
            x, y = q.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not (0 <= nx < n and 0 <= ny < n):
                    continue

                if (nx, ny) in visited:
                    continue

                if board[x][y] + 1 == board[nx][ny]:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    cnt += 1

        return cnt


    max_cnt = -1
    max_pos = 10**10
    for i in range(n):
        for j in range(n):
            score = bfs(i, j)
            if max_cnt < score:
                max_cnt = score
                max_pos = board[i][j]
            elif max_cnt == score:
                max_pos = min(board[i][j], max_pos)

    print(f"#{tc} {max_pos} {max_cnt}")
