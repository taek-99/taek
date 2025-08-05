from collections import deque

# 3시간 동안 고민해도 안되서 유튜브 참고했습니다....
# 런타임 너무 오래 걸려서 프로그램 업데이트 예정

n, m, v = map(int, input().split())
num = [list(map(int, input().split())) for i in range (m)]
board = [[False] * (n+1) for i in range (n+1)]
visited = [False] * (n+1)


# dfs
def sol_dfs(x):
    for i in range (1, n+1):
        if not visited[i] and board[x][i]:
            visited[i] = True
            ans.append(i)
            sol_dfs(i)

# 그래프 생성
for x, y in num:
    board[x][y] = True
    board[y][x] = True

ans = []
visited[v] = True
ans.append(v)
sol_dfs(v)
for i in ans:
    print (i, end=" ")
print ()


visited = [False] * (n+1)
ans = []
q = deque([])
q.append(v)

# bfs
while q:
    dq = q.popleft()
    for i in range (1, n+1):
        if not visited[i] and board[dq][i]:
            q.append(i)

    if not visited[dq]:
        visited[dq] = True
        ans.append(dq)

for i in ans:
    print (i, end=" ")