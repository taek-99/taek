import copy
from itertools import product

T = int(input())

for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(h)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def sol (x, y, z):
        for jj in range(1, z):
            for ii in range(4):
                nx = x + (dx[ii]*jj)
                ny = y + (dy[ii]*jj)
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny]:
                    nbomb = board[nx][ny]
                    board[nx][ny] = 0
                    sol (nx, ny, nbomb)
    
    def sol_move():
        for ii in range (w):
            for jj in range(h-1, -1, -1):
                if not board[jj][ii]:
                    for k in range(jj, -1, -1):
                        if board[k][ii]:
                            board[jj][ii] = board[k][ii]
                            board[k][ii] = 0
                            break
    
    min_sum = 10**9
    for pos in product(range(w), repeat=n):
        board = copy.deepcopy(brick)
        for y in pos:
            for x in range(h):
                if board[x][y]:
                    bomb = board[x][y]
                    board[x][y] = 0
                    sol (x, y, bomb)
                    sol_move()
                    break
        
        sum_ans = 0
        for i in range(h):
            for j in range(w):
                if board[i][j]:
                    sum_ans += 1
        
        if min_sum > sum_ans:
            min_sum = sum_ans
    
    print (f"#{tc} {min_sum}")