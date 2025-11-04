from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
shark = 2
food = 0
ans = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sh_r, sh_c = i, j
            break


q = deque()
q.append((sh_r, sh_c))
visited[sh_r][sh_c] = True
board[sh_r][sh_c] = 0
tt = 0

             
while q:

    tt += 1
    eat_food = False
    tx = ty = None
    for _ in range(len(q)):
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not(0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                continue
            
            if shark < board[nx][ny]:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny))

            if 0 < board[nx][ny] < shark:  ## 초기화해라
                if not eat_food:
                    eat_food = True
                    tx, ty = nx, ny
                else:
                    if (nx < tx) or (nx == tx and ny < ty):
                        tx, ty = nx, ny

    if eat_food:
        ans += tt
        tt = 0
        food += 1

        sh_r, sh_c = tx, ty
        board[tx][ty] = 0  # ★ 먹은 칸만 0으로 (중복 제거)

        # 크기 증가 체크
        if food == shark:
            shark += 1
            food = 0

        # BFS 리셋
        visited = [[False] * n for _ in range(n)]
        visited[sh_r][sh_c] = True
        q = deque()
        q.append((sh_r, sh_c))
        continue

    
print(ans)