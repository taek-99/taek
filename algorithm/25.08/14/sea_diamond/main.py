import sys
sys.stdin = open('sample_input (27).txt','r')
from collections import deque


T = int(input())
for tc in range(1, T+1):
    k = input()
    str_length = len(k)
    n = 5
    m = n * str_length - (str_length - 1)
    str_str = deque(k)

    if len(k) == 1:
        board = [["."] * n for _ in range(n) ]
    else:
        board = [["."] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or i == 4: #위, 아래 양끝
                if j == 2 or (j -2) % 4 == 0:
                    board[i][j] = "#"
            if i == 2: # 중앙
                if j == 2 or (j - 2) % 4 == 0:
                    board[i][j] = str_str.popleft()
                if j == 0 or j == m - 1 or j % 4 == 0:
                    board[i][j] = "#"

            if i == 1 or i == 3: # 그 사이
                if j % 2 == 1:
                    board[i][j] = '#'

    for i in range(n):
        print (''.join(board[i]))

