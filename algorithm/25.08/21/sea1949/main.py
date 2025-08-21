import sys
sys.stdin = open('sample_input (4).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    max_num = 0
    for i in range(n):  # 가장 큰값 찾기
        for j in range(n):
            max_num = max(board[i][j], max_num)

    start_pos = []
    for i in range(n):  # 시작 포인트 넣기
        for j in range(n):
            if board[i][j] == max_num:
                start_pos.append((i, j))

    def dfs(pos, cnt, used):  # 좌표, 거리, 컷팅여부, 보드
        global max_cnt
        x = pos[0]
        y = pos[1]
        visited[x][y] = True
        pos_data = board[x][y]
        move = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                next_data = board[nx][ny]
                if next_data < pos_data:  # 다음 위치가 내 위치보다 작으면 이동
                    move = True
                    dfs((nx, ny), cnt + 1, used)
                elif next_data >= pos_data and not used:  # 다음 위치가 내 위치보다 크면서 컷팅 안했어야함
                    for ii in range(1, k+1):
                        if next_data - ii < pos_data:  # 컷팅했을때 나보다 작아지면 이동
                            move = True
                            board[nx][ny] -= ii
                            dfs((nx, ny), cnt + 1, True)
                            board[nx][ny] += ii

        visited[x][y] = False
        if not move:
            max_cnt = max(max_cnt, cnt)
            return


    max_cnt = 0
    for i, j in start_pos:
        dfs((i, j), 1, False)

    print(f"#{tc} {max_cnt}")