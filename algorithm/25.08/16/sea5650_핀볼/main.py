T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split()))for _ in range(n)]
    
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    block_dict = { # 벽 종류별 부딪혔을때 이동 방향
            1 : [1, 3, 0, 2],
            2 : [3, 0, 1, 2],
            3 : [2, 0, 3, 1],
            4 : [1, 2, 3, 0],
            5 : [1, 0, 3, 2]
        }
    
    worm_dict = {
        6 : [],
        7 : [],
        8 : [],
        9 : [],
        10: []    
    } 
    
    
    for i in range(n):
        for j in range(n):
            if board[i][j] > 5:
                worm_dict[board[i][j]].append((i, j))
    
    hole_dict = {}
    for v in worm_dict.values():
        if v:
            hole_dict[(v[0])] = v[1]
            hole_dict[(v[1])] = v[0]
    
    
    
    def dfs(x, y, d):
        global max_point
        sx = x
        sy = y
        
        score = 0
        while True:
    
            nx = x + dx[d]
            ny = y + dy[d]
    
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 5:
                score += 1
                d = block_dict[5][d]
                x, y = nx, ny
                continue
        
            if nx == sx and ny == sy or board[nx][ny] == -1:
                break
    
            if 0 < board[nx][ny] < 5:
                score += 1
                d = block_dict[board[nx][ny]][d]
                x, y = nx, ny
                continue
    
            if 5 < board[nx][ny]:
                x, y = hole_dict[(nx, ny)]
                continue
    
            x, y = nx, ny 
    
        max_point = max(max_point, score)
    
    max_point = 0
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                for ii in range(4):
                    dfs (i, j, ii)
    
    
    print (f"#{tc} {max_point}")