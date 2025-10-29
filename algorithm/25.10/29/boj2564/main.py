from pprint import pprint
from collections import deque

n, m = map(int, input().split())
board = [[False] * n for _ in range(m)]
new_board = [[0] * n for _ in range(m)]

k = int(input())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cw = [1, 3, 0, 2]
ccw = [0, 3, 1, 2]

##  1북, 2남, 3서, 4동
for _ in range(k):
    d, g = map(int, input().split())
    if d == 1:
        r = 0
        c = g-1

    if d == 2:
        r = m-1
        c = g-1

    if d == 3:
        r = g-1
        c = 0

    if d == 4:
        r = g-1
        c = n-1

    arr.append((r, c))
    board[r][c] = True


d, g = map(int, input().split())

if d == 1:
    r = 0
    c = g-1

if d == 2:
    r = m-1
    c = g-1

if d == 3:
    r = g-1
    c = 0

if d == 4:
    r = g-1
    c = n-1

st_r = r
st_c = c

pprint (board)
## ====================================================
ans = 0
visited = set()

tt = 1
x = st_r
y = st_c
di = 0

while tt:
    nx = x + dx[cw[di]]
    ny = y + dy[cw[di]]

    if (nx, ny) == (st_r, st_c):
        break

    if not(0 <= nx < m and 0 <= ny < n):
        di += 1
        if di == 4:
            di = 0
        continue

    x, y = nx, ny
    tt += 1
    
    if (nx, ny) in arr:
        if not new_board[nx][ny]:
            new_board[nx][ny] = tt
        else:
            new_board[nx][ny] = min(new_board[nx][ny], tt)   


pprint(new_board)


tt = 1
x = st_r
y = st_c
di = 3
print (ccw)
while tt:
    nx = x + dx[ccw[di]]
    ny = y + dy[ccw[di]]

    if (nx, ny) == (st_r, st_c):
        break

    if not(0 <= nx < m and 0 <= ny < n):
        di += 1
        if di == 4:
            di = 0
        continue
    
    print (nx, ny)
    x, y = nx, ny
    tt += 1
    
    if (nx, ny) in arr:
        if not new_board[nx][ny]:
            new_board[nx][ny] = tt
        else:
            new_board[nx][ny] = min(new_board[nx][ny], tt)  

pprint(new_board)