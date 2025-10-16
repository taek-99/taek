import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]:
            visited[i][j] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tt = 1


def glacier():

    for i in range(n):
        for j in range(m):
            if board[i][j]:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if not(0 <= nx < n and 0 <= ny < m) or board[nx][ny]:
                        continue

                    bd[i][j] -= 1
                    if not bd[i][j]:
                        visited[i][j] = False
                        break

    return bd


def bfs():
    cnt = 0

    for i in range(n):
        for j in range(m):
            if new_visited[i][j]:

                q = deque()
                q.append((i, j))
                cnt += 1
                new_visited[i][j] = False

                while q:
                    x, y = q.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if not(0 <= nx < n and 0 <= ny < m) or not new_visited[nx][ny]:
                            continue

                        q.append((nx, ny))
                        new_visited[nx][ny] = False

    return cnt
    

while tt:

    bd = [val[:] for val in board]
    board = glacier()

    new_visited = [val[:] for val in visited]
    if bfs() >= 2:
        print (tt)
        break

    tt += 1

# ##
# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0
# ##