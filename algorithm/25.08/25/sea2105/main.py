import sys
sys.stdin = open('taek/algorithm/25.08/25/sea2105/sample_input (30).txt','r')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]


    def sol(pos, dx, dy, score):
        global max_num, sx, sy

        x = pos[0]
        y = pos[1]
        if (dx, dy) == (-1, 1) and (x-1, y+1) == (sx, sy):
            max_num = max(max_num, len(score))
            return

        nx = x + dx
        ny = y + dy
            
        if 0 <= nx < n and 0 <= ny < n :
            if board[nx][ny] not in score:
                score.append(board[nx][ny])
                sol((nx, ny), dx, dy, score)
                score.pop()
            
        if (dx, dy) == (1, 1) and len(score) > 1:
            sol ((x, y), 1, -1, score)

        if (dx, dy) == (1, -1) and len(score) > 2:
            sol ((x, y), -1, -1, score)
 
        if (dx, dy) == (-1, -1) and len(score) > 3:
            sol ((x, y), -1, 1, score)


    max_num = -1
    for i in range(n):
        for j in range(n):
            sx = i
            sy = j
            sol ((i, j), 1, 1, [board[i][j]])

    print (f"#{tc} {max_num}")