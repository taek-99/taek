T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def sol(x, y):
        global max_home
        visited[x][y] = True
        k = 0
        home = 0
        pos_list = []
        while True:
            k += 1
            cost = k * k + (k - 1) * (k - 1)
            if k == 1:
                if board[x][y] == 1:
                    home += 1
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        pos_list.append ((nx, ny))
            elif k == 2:
                for hx, hy in pos_list:
                    if 0 <= hx < n and 0 <= hy < n and not visited[hx][hy]:
                        visited[hx][hy] = True
                        if board[hx][hy]:
                            home += 1               
            else:
                new_list = []
                for hx, hy in pos_list:
                    for d in range(4):
                        nx = hx + dx[d]
                        ny = hy + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            visited[nx][ny] = True
                            new_list.append((nx, ny))
                            if board[nx][ny]:
                                home += 1
                pos_list = new_list
                                
            if m * home >= cost:
                max_home = max(max_home, home)
    
            if k == n+1:
                break
    
    max_home = 0
    for i in range(n):
        for j in range(n):
            visited = [[False] * n for _ in range(n)]
            sol (i, j)

    print (f"#{tc} {max_home}")