n, m = map(int,input().split())
board = [list(map(str, input())) for _ in range (n)]

dx = [0, 1, 1]
dy = [1, 1, 0]

aaa = min(n,m)
ans = 0

def sol(x, y, sq):
    global ans
    
    for ii in range (aaa):
        sq_list = []
        for jj in range (3):
            nx = x + dx[jj] * ii
            ny = y + dy[jj] * ii
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == sq:
                sq_list.append(board[nx][ny])
        if all(sq == k for k in sq_list) and len(sq_list) == 3 and ii > ans:
            ans = ii

for i in range (n):
    for j in range (m):
        sol (i, j, board[i][j])
        
        
print ((ans+1) * (ans+1))




