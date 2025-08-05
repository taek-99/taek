t = int(input())

for tc in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * n for i in range (m)]
    
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    for _ in range(k):
        x, y = map(int,input().split())
        board[x][y] = 1
    
    def sol(x, y):
        for ii in range (4):
            nx = x + dx[ii]
            ny = y + dy[ii]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny]:
                board[nx][ny] = 0
                sol (nx, ny)
                
    ans = 0
    for i in range (m):
        for j in range (n):
            if board[i][j]:
                board [i][j] = 0
                ans += 1
                sol (i, j)

    print (ans)