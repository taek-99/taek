t = int(input())

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


for tc in range (t):
    n = int(input())
    board = [list(input()) for i in range (n)]
    
    def sol(x, y, z):
        for jj in range (8): #8방향 확인
            cnt = 0
            for ii in range (1, 5): #해당 방향에 4개 더 있는 지 확인
                nx = x + dx[jj] * ii
                ny = y + dy[jj] * ii
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == "o":
                        cnt += 1
            if cnt == 4:
                return cnt
        return cnt              
        
    aaa = "NO"
    ans = 0
    for i in range (n):
        for j in range (n):
            if board[i][j] == "o":
                ans = sol(i, j, board[i][j])
            if ans == 4:
                aaa = "YES"
                break
        if ans == 4:
            break
    
    print (f"#{tc+1} {aaa}")
            