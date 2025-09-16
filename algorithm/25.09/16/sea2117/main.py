import sys
sys.stdin = open('sample_input (13).txt' , 'r')


from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    def dfs(pos):
        global max_num
        new_pos_list = deque()
        pos_list = deque()
        record_pos = set()
        new_pos_list.append((pos[0], pos[1]))
        home_cnt = board[pos[0]][pos[1]]
        record_pos.add((pos[0], pos[1]))

        k = 0
        while k < n+2:
            k += 1
            cost = k * k + (k-1) * (k-1)
            if k > 1:
                pos_list = new_pos_list
                new_pos_list = deque()
                while pos_list:
                    x, y = pos_list.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in record_pos:
                            continue

                        new_pos_list.append((nx, ny))
                        record_pos.add((nx, ny))
                        if board[nx][ny] == 1:
                            home_cnt += 1

            if cost <= home_cnt * m:
                max_num = max(max_num, home_cnt)


    max_num = 0
    for i in range(n):
        for j in range(n):
            dfs((i, j))

    print(f"#{tc} {max_num}")