num = int(input())
rail = [list(map(int, input().split())) for i in range (num)]
start = list(map(int, input().split()))
end = list(map(int, input().split()))

board = [[0]*num for i in range(num)]
swl = []
visitor = [[False]*num for i in range(num)]

board = rail

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 주변에 자리에 +1 더해주기
def sol (x, y):
    for jj in range (4):
        nx = x + dx[jj]
        ny = y + dy[jj]
        if 0 <= nx < num and 0 <= ny < num and visitor[nx][ny] == False and board[nx][ny] == 0:
            board[nx][ny] = board[x][y]+1
            visitor[nx][ny] = True
            print (board)

# 장애물 위치에 True, 소용돌이는  넣기
for i in range (num):
    for j in range (num):
        if board[i][j] == 1:
            board[i][j] = -999
            visitor[i][j] = True
            
        if board[i][j] == 2:
            board[i][j] = 0
            visitor[i][j] = True
            swl.append([i, j])


# 시작지점 세팅
s, t = start
board[s][t] = 1
visitor[s][t] = True
sol (s, t)

for ii in range (1, num*num):
# 2초 마다 소용돌이 on, off
    if ii%2 == 0:
        for aa, bb in swl:
            if visitor[aa][bb] == True:
                visitor[aa][bb] = False
            else:
                visitor[aa][bb] = True

# 목적지까지 길 구하기 sol 이동

    cnt = False
    for i in range (num):
        for j in range (num):
            if board[i][j] > 0:
                sol (i, j)
                
                
print (board)