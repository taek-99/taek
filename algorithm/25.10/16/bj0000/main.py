from collections import deque


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]


def water_bam():
    for i in range(n):
        for j in range(n):
            if board[i][j] == tt:
                visited[i][j] = True


def bfs():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if new_visited[i][j]:
                continue

            cnt += 1
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if not(0 <= nx < n and 0 <= ny < n) or new_visited[nx][ny]:
                        continue

                    q.append((nx, ny))
                    new_visited[nx][ny] = True

    return cnt

max_ans = 0
tt = 0

while tt <= 100:

    water_bam()
    new_visited = [val[:] for val in visited]  # 방문처리용
    max_ans = max(max_ans, bfs())

    tt += 1

print (max_ans)

