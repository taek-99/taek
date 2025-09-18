import sys
sys.stdin = open('sample_input (14).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = 4
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans_list = set()


    def dfs(x, y, idx, num):
        global ans_list

        if idx == 8:
            if num not in ans_list:
                ans_list.add(num)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0 <= nx < n and 0 <= ny < n):
                continue

            dfs(nx, ny, idx+1, num+str(board[nx][ny]))


    for i in range(n):
        for j in range(n):
            dfs(i, j, 1, "")

    print(f"#{tc} {len(ans_list)}")