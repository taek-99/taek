from collections import deque

T = int(input())

for tt in range (T):
    n, m = map(int, input().split())
    board = [list(input()) for i in range (n)]
    num = int(input())
    move = deque(input())
    aaa = max (n,m)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dir = 0
    
    # 상0, 하1, 좌2, 우3
    # 해당 방향으로 이동
    def sol_dir(x, y, z):
        # 머리 방향 먼저 돌림
        if z == 0 :
            board[x][y] = "^"
        if z == 1 :
            board[x][y] = "v"
        if z == 2 :
            board[x][y] = "<"
        if z == 3 :
            board[x][y] = ">"
    
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == ".":
                if z == 0:
                    board[nx][ny] = "^"
                if z == 1:
                    board[nx][ny] = "v"
                if z == 2:
                    board[nx][ny] = "<"
                if z == 3:
                    board[nx][ny] = ">"
                board[x][y] = "."
                return nx, ny, z
        return x, y, z
        
    # 포탄 발사
    def attack(x, y, z):
        for i in range(1, aaa+1):
            nx = x + dx[z] * i
            ny = y + dy[z] * i
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "*":
                    board[nx][ny] = "."
                    break
                if board[nx][ny] == "#":
                    break
                    
    # main/ 시작 위치 찾기    
    talchul = True
    pos_x = 0
    pos_y = 0
    for i in range (n):
        for j in range (m):
            if board[i][j] == "^" or board[i][j] == "v" or board[i][j] == "<" or board[i][j] == ">":
                if board[i][j] == "^":
                    dir = 0
                if board[i][j] == "v":
                    dir = 1
                if board[i][j] == "<":
                    dir = 2
                if board[i][j] == ">":
                    dir = 3
                pos_x = i
                pos_y = j
    
    
    while move:
        dq = move.popleft()
        if dq == "S":
            attack(pos_x, pos_y, dir)
        if dq == "U":
            pos_x, pos_y, dir = sol_dir(pos_x, pos_y, 0)
        if dq == "D":
            pos_x, pos_y, dir = sol_dir(pos_x, pos_y, 1)
        if dq == "L":
            pos_x, pos_y, dir = sol_dir(pos_x, pos_y, 2)
        if dq == "R":
            pos_x, pos_y, dir = sol_dir(pos_x, pos_y, 3)
        
    for j in range(n):
        if j == 0:
            print (f"#{tt+1} ", end="")
        for i in board[j]:
            print (i, end="")
        print("")
        