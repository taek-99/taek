n = int(input())
ans = 0

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def dfs(pos, visit):
    global ans, ans_list

    x = pos[0]
    y = pos[1]
    visit[x][y] = True

    for ii in range(1, n): # 퀸 놨음
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True

    for ii in range(pos[0], n): # 다음 놀곳 탐색
        for jj in range(pos[1], n):
            if not visit[ii][jj]:
                dfs((ii, jj), visit)

    if all(visit[x][y] for x in range(n) for y in range(n)):
        ans += 1
        return

ans_list = []
for i in range(n):
    for j in range(n):
        visited = [[False] * n for _ in range(n)]
        pos_list = []
        dfs((i, j), visited)

print (ans)