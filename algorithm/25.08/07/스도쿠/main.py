import sys
sys.stdin = open("input (7).txt", "r")

T = int(input())

for tc in range (1, T+1):
    board = [list(map(int, input().split())) for _ in range (9)]
    ans = 1

    for i in range (9): # 가로
        for j in range (1, 10):
            if board[i].count(j) != 1:
                ans = 0
                break
        if not ans:
            break

    if ans:  #새로
        for i in range (9):
            new_board = []
            for j in range (9): #확인용 새보드에 넣음
                new_board.append(board[j][i])
            for k in range (1, 10):
                if new_board.count(k) != 1:
                    ans = 0
                    break
            if not ans:
                break

    if ans: #각 구역
        for i in range (0, 9, 3):
            for j in range (0, 9, 3):
                new_board = []
                for ii in range (3):
                    for jj in range (3):
                        new_board.append(board[i+ii][j+jj])
                for kk in range (1, 10):
                    if new_board.count(kk) != 1:
                        ans = 0
                        break
                if not ans:
                    break
            if not ans:
                break

    print (f"#{tc} {ans}")