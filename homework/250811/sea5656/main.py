import sys
from itertools import product

T = int(input())
n, w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def sol (x, y, z):
    for jj in range(z):
        for ii in range(4):
            nx = x + (dx[ii]*jj)
            ny = y + (dy[ii]*jj)
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny]:
                nbomb = board[nx][ny]
                board[nx][ny] = 0
                sol (nx, ny, nbomb)

def sol_move():
    for ii in range (w):
        for jj in range(h):
            if not board[jj][ii]:
                for k in range(jj, h):
                    if board[k][ii]:
                        board[jj][ii] = board[k][ii]
                        board[k][ii] = 0

cnt = 0
for pos in product(range(w), repeat=n):
    ans = 0
    for y in pos:
        for x in range(h, -1, -1):
            if board[x][y]:
                bomb = board[x][y]
                board[x][y] = 0
                sol (x, y, bomb)
                sol_move()

sum_ans = 0
for i in range(h):
    for j in range(w):
        if board[i][j]:
            sum_ans += board[i][j]

print (sum_ans)