

n, m = map(int, input().split())
k = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = [[False] * n for _ in range(m)]

x = 0
y = 0
d = 0
tt = 0
cnt = 1

while cnt <= (n * m):

    nx = x + dx[d]
    ny = y + dy[d]

    board[x][y] = True
    
    if cnt == k:
        print(y+1, x+1)
        exit()
    cnt += 1

    if not (0 <= nx < m and 0 <= ny < n) or board[nx][ny]:
        d = (d+1) % 4
        continue

    x, y = nx, ny

print (0)

