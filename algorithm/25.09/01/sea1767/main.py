import sys
sys.stdin = open('taek/algorithm/25.09/01/sea1767/sample_input (39).txt','r')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cell_list = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if board[i][j]:
                cell_list.append((i, j))


    def sol(ph, new_bd):
        for x, y in ph:
            new_bd[x][y] = 0

    def dfs(idx, connetion, wire, bd):
        global max_con, min_wire

        if idx == len(cell_list):
            if connetion > max_con:
                max_con = connetion
                min_wire = wire
            elif connetion == max_con:
                max_con = max(max_con, connetion)
                min_wire = min(min_wire, wire)
            return

        x, y = cell_list[idx]
        for d in range(4):
            path = []
            for k in range(1, n):
                nx = x + dx[d] * k
                ny = y + dy[d] * k

                if not (0 <= nx < n and 0 <= ny < n):
                    sol(path, bd)
                    break

                if bd[nx][ny]:
                    sol(path, bd)
                    break

                path.append ((nx, ny))
                bd[nx][ny] = idx + 1

                if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                    dfs(idx+1, connetion+1, wire+k, bd)    
                    sol(path, bd)
        
        
        dfs(idx+1, connetion, wire, bd)
                    
                
    max_con = 0
    min_wire = 10 ** 10
    dfs (0, 0, 0, board)

    print (f"#{tc} {min_wire}")