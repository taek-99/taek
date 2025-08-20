from collections import deque

T = int(input())

for tc in range (T):
    N, M = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    home_set = set()
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                home_set.add((i, j)) 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans_list = set()
    ans_list.add(1)

    for x in range (N):
        for y in range (N):
            q = deque()
            q.append((x, y))
            visited = [[False] * N for _ in range (N)]
            visited[x][y] = True
            K = 1
            cnt = 1 if (x, y) in home_set else 0 
            ans = 0
            while q:
                cost = K * K + (K - 1) * (K - 1)
                if cnt * M >= cost:
                    ans = max(ans, cnt)
    
                size = len(q)
                for _ in range (size):
                    (nx, ny) = q.popleft()
                    for ii in range (4):
                        xx = nx + dx[ii]
                        yy = ny + dy[ii]
                        if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy]:
                            q.append((xx, yy))
                            visited[xx][yy] = True
                            if (xx, yy) in home_set:
                                cnt += 1
                            
                K += 1
                if K > N + 1:
                    break
            ans_list.add(ans)
    print(f"#{tc+1} {max(ans_list)}")
