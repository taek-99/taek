import copy

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]

def answer():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    return False
    
    return True


if answer ():
    print (0)
    exit()

tt = 1
while True:
    tomato = False

    tomato_board = copy.deepcopy(board)
    for i in range(h):
        for j in range(n):
            for k in range(m):
                # print (i, j, k)
                if tomato_board[i][j][k] == 1 and not visited[i][j][k]:
                    tomato = True
                    visited[i][j][k] = True

                    for d in range(4):  # 앞, 뒤, 좌, 우
                        nx = j + dx[d]
                        ny = k + dy[d]

                        if not (0 <= nx < n and 0 <= ny < m):
                            continue

                        if board[i][nx][ny] == 0:
                            board[i][nx][ny] = 1


                    for d in range(2):  # 위, 아래
                        nz = i + dz[d]
                        if not (0 <= nz < h):
                            continue
                        
                        if board[nz][j][k] == 0:
                            board[nz][j][k] = 1


   
    if answer ():
        print (tt)
        break
    else:
        if not tomato:
            print (-1)
            break

    tt += 1
