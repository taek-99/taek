
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
walk_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

not_break_visited = [bytearray(m) for _ in range(n)]
break_visited = [bytearray(m) for _ in range(n)]

q = deque()
q.append((0, 0, 0))

tt = 1
while q:
    for _ in range(len(q)):
        x, y, val = q.popleft()

        if x == n -1 and y == m - 1:
            print (not_break_visited)
            print (break_visited)
            print (tt)
            exit()

        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not(0 <= nx < n and 0 <= ny < m):
                continue

            if board[nx][ny] == 0:
                if val == 0 and not not_break_visited[nx][ny]:
                    not_break_visited[nx][ny] = 1
                    q.append((nx, ny, 0))
                elif val == 1 and not break_visited[nx][ny]:
                    break_visited[nx][ny] = 1
                    q.append((nx, ny, 1))
            else:  
                if val == 0 and not break_visited[nx][ny]:
                    break_visited[nx][ny] = 1
                    q.append((nx, ny, 1))
    
    tt += 1

print (-1)