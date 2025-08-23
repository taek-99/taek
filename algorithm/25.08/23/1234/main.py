import sys
sys.stdin = open('taek/algorithm/25.08/23/1234/input (13).txt','r')


for tc in range(1, 11):
    T = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    
    for i in range(100):
        if board[99][i] == 2:
            sx, sy = 99, i
            break
    
    x, y = sx, sy
    while x:
        visited[x][y] = True
        for ii in range(3):
            nx = x + dx[ii]
            ny = y + dy[ii]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    x, y = nx, ny
                    break
    
    print (f"#{tc} {y}")