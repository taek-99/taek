import sys
sys.stdin = open('sample_input (2).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dir_change = [1, 0, 3, 2]

    block_dict ={
        1: [1, 3, 0, 2],
        2: [3, 0, 1, 2],
        3: [2, 0, 3, 1],
        4: [1, 2, 3, 0],
        5: [1, 0, 2, 3]
    }

    worm = {
        6: [],
        7: [],
        8: [],
        9: [],
        10: []
    }

    for i in range(n):
        for j in range(n):
            if board[i][j] > 5:
                worm[board[i][j]].append((i, j))

    hole_list = {}
    for val in worm.values():
        if val:
            hole_list[val[0]] = val[1]
            hole_list[val[1]] = val[0]


    def dfs(pos, d):
        global max_num

        sx = pos[0]
        sy = pos[1]
        x = pos[0]
        y = pos[1]
        score = 0

        while True:
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 5:  # 외곽이나 5인 벽에 부딪혔을 때
                d = dir_change[d]
                score += 1
                x, y = nx, ny
                continue

            if nx == sx and ny == sy or board[nx][ny] == -1:  # 시작포인트에 왔거나 블랙홀 도착시 종료
                max_num = max(max_num, score)
                break

            if 0 < board[nx][ny] < 5:  # 1~4 벽에 부딪혔을 때
                d = block_dict[board[nx][ny]][d]
                x, y = nx, ny
                score += 1
                continue

            if 5 < board[nx][ny]: # 웜홀에 빠지면
                x, y = hole_list[(nx, ny)]
                continue

            x, y = nx, ny


    max_num = 0
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                for ii in range(4):
                    dfs((i, j), ii)

    print (f"#{tc} {max_num}")
