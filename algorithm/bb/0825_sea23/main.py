import sys
sys.stdin = open('sample_input (32).txt','r')


T, score = map(int, input().split())
nn = int(input())
k, n, m = map(int, input().split())

star_list = []
for i in range(n):  # 2진수 변환 후 리스트에 저장
    a = int(input())
    s = bin(a)[2:]
    s = s.zfill(25)
    star_list.append(s)

print (star_list)
# ==================================================================================
h = 0
r_len = len(star_list)
c_len = len(star_list[0])
star_board = [[0]*(c_len+1) for _ in range(r_len+1)]

for r in range(1, r_len+1):  # 누적합 해놓기
    row_acc = 0
    for c in range(1, c_len+1):
        row_acc += int(star_list[r-1][c-1])
        star_board[r][c] = star_board[r-1][c] + row_acc

print (star_board)
# ==============================================================================
for r in range(5, r_len+1):  # 각 구역별 별이 몇개 있는지 & 타일이 맞는지
    for c in range(5, c_len+1):
        star_cnt = star_board[r][c] - star_board[r-5][c] - star_board[r][c-5] + star_board[r-5][c-5]
        if star_cnt == 7:
            print ("ji")
