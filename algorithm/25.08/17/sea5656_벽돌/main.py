## 12:15
## 12:40

## 13:33

import copy
from collections import deque
T = int(input())

for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    def bomb(bd, xx, yy, zz):
        bomb_list = deque()
        bomb_list.append ((xx, yy, zz))
        bd[xx][yy] = 0
    
        while bomb_list:
            bx, by, data = bomb_list.popleft()
            if data <= 1:
                continue
    
            for d in range(4):
                nx, ny = bx, by
                for _ in range(data-1):
                    nx += dx[d]
                    ny += dy[d]
                    if not (0 <= nx < h and 0 <= ny < w):
                        break
                    if bd[nx][ny] == 0:
                        continue
                    bomb_list.append((nx, ny, bd[nx][ny]))
                    bd[nx][ny] = 0
    
    def gravity(bd):
        for ii in range(w): # 폭파후 중력에 의해 벽돌 내려옴
            new_list = []
            for jj in range(h-1, -1, -1):
                if bd[jj][ii]:
                    new_list.append(bd[jj][ii])
                    bd[jj][ii] = 0
            if new_list:
                for k in range(len(new_list)):
                    bd[h-k-1][ii] = new_list[k]

                
    def dfs (shoot, bd):
        global min_brick
    
        if shoot == 0: #공을 다 쐈을 경우 갯수 확인
            cnt = 0
            for i in range(h):
                for j in range(w):
                    if bd[i][j]:
                        cnt += 1
            min_brick = min(min_brick, cnt)
            return
    
        for i in range(w):
            new_board = copy.deepcopy(bd)
            for j in range(h):
                if new_board[j][i]:
                    bomb(new_board, j, i, new_board[j][i]) #공을 쏜 열에 블록 확인
                    gravity(new_board)
                    dfs(shoot-1, new_board)
                    break
            else:
                dfs(shoot-1, new_board)

    min_brick = 10**10
    dfs(n, board) #pos, 공쏘는 갯수
    
    print (f"#{tc} {min_brick}")