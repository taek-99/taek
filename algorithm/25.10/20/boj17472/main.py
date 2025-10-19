
from collections import deque, defaultdict


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
island_list = [[(-1, -1)] * m for _ in range(n)]
p_list = []
island_dict = defaultdict(list)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def union_find(r, c):
    q = deque()
    q.append((r, c))

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        island_dict[(r, c)].append((x, y))

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue

            if board[nx][ny]:    
                island_list[nx][ny] = (r, c)
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            island_list[i][j] = (i, j)
            p_list.append((i, j))
            union_find(i, j)


def dfs(r, c):

    for d in range(4):
        nx = r + dx[d]
        ny = c + dy[d]

        if not (0 <= nx < n and 0 <= ny < m ):
            continue
            
        if board[nx][ny]:
            continue


while True:
    for pos, val in island_dict.items():
        r, c = val.pop()
        if not dfs(r, c):
            break
    
    if all(p_list) == p_list[0]:
        break


