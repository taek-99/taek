
from collections import deque

n = 10
board = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
st_x = st_y = 0
ed_x = ed_y = n-1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


q = deque()
neq_q = deque()
neq_q.append((st_x, st_y))
visited[st_x][st_y] = True


for k in range(1, 2 * n):
    q = neq_q
    neq_q = deque()
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not(0 <= nx < n and 0 <= ny < n):
                continue

            if not visited[nx][ny] and (nx, ny) not in neq_q:
                neq_q.append((nx, ny))
                board[nx][ny] = k
    
    if (ed_x, ed_y) in neq_q:
        break

    for (x, y) in neq_q:
        visited[x][y] = True



if board[ed_x][ed_y] > 0:
    ans_pos = []
    x, y = ed_x, ed_y
    for k in range(board[ed_x][ed_y]-1, -1, -1):
        ans_pos.append((x, y))
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            
            if board[nx][ny] == k:
                x, y = nx, ny
                break
            
    print (ans_pos[::-1])