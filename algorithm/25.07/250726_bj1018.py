n, m = map(int, input(). split())
board = [list(input()) for i in range (n)]

b_board = [["B"]*8 for i in range (8)]
w_board = [["W"]*8 for i in range (8)]

for i in range (8):
    for j in range (8):
        if i % 2 == 0:
            if j % 2 == 0:
                b_board[i][j] = "W"
                w_board[i][j] = "B"
        else:
            if j % 2 == 1:
                b_board[i][j] = "W"
                w_board[i][j] = "B"

# 흑과 백의 카운트 갯수 선언
def sol(x, y):
    w_cnt = 0
    b_cnt = 0
    
    # 8x8판의 w와 b의 갯수 비교
    for ii in range (8):
        for jj in range (8):
            nx = x + ii
            ny = y + jj
            if board[nx][ny] != w_board[ii][jj]:
                w_cnt += 1
            if board[nx][ny] != b_board[ii][jj]:
                b_cnt += 1

    return (min(w_cnt, b_cnt))

ans = []
# 횡, 종 -8만큼만 for문 돌리기 위함
for i in range (n-7):
    for j in range (m-7):
        ans.append(sol(i, j))

print (min(ans))