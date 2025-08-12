import sys
sys.stdin = open('sample_input (24).txt','r')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split()))for _ in range(n)]

    max_num = -1
    start_point = []
    for i in range(n): # 시작점을 위한 큰값과 좌표 저장, 종료조건을 위한 작은값 저장
        for j in range(n):
            if board[i][j] > max_num:
                max_num = board[i][j]
                start_point = []
            if board[i][j] == max_num:
                start_point.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * n for _ in range(n)]

    def dfs(x, y, hiking_trail, used_cut):
        visited[x][y] = True
        high_point = board[x][y]
        best = hiking_trail
        for ii in range(4):
            nx = x + dx[ii]
            ny = y + dy[ii]
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                continue

            nh = board[nx][ny]

            if nh < high_point:
                best = max(best, dfs(nx, ny, hiking_trail+1, used_cut))

            elif not used_cut and nh - k < high_point:
                tempory = board[nx][ny]
                for cut in range(1, k+1):
                    if nh - cut < high_point:
                        board[nx][ny] = nh - cut
                        best = max(best, dfs(nx, ny, hiking_trail+1, True))
                        board[nx][ny] = tempory

        visited[x][y] = False
        return best

    max_ans = 0
    for sx, sy in start_point:
        ans = dfs(sx, sy, 1, False)
        if ans > max_ans:
            max_ans = ans

    print (f"#{tc} {max_ans}")