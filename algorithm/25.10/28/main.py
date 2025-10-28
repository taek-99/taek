
from collections import deque

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]

def ans():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    return False
    return True

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i, j, k))


tt = 1
new_q = deque()
while tt:
    new_q = q
    q = deque()

    while new_q:
        z, x, y = new_q.popleft()

        for d in range(4):  # 앞, 뒤, 좌, 우
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if board[z][nx][ny] == 0:
                board[z][nx][ny] = 1
                q.append((z, nx, ny))
            
        for d in range(2):  # 위, 아래
            nz = z + dz[d]
            if not (0 <= nz < h):
                continue

            if board[nz][x][y] == 0:
                board[nz][x][y] = 1
                q.append((nz, x, y))

    if not q: 
        if ans():
            print (tt-1)
        else:
            print (-1)
        break

    tt += 1