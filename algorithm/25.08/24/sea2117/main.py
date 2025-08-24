import sys
sys.stdin = open('taek/algorithm/25.08/24/sea2117/sample_input (30).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]


    def sol(x, y):
        global max_num

        for k in range(1, 2*n+1):
            r = k -1
            house = 0
            cnt = 0
            tp = 1
            for nx in range(x-r, x+r+1): # 상,하
                for ny in range(y-cnt, y+cnt+1):
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny]:
                            house += 1      
                cnt += 1*tp
                if cnt == r:
                    tp = -1

            cost = k * k + (k - 1) * (k - 1)
            if cost <= m * house:
                max_num = max(max_num, house)

    max_num = 0
    for i in range(n):
        for j in range(n):
            sol (i, j)

    print (f"#{tc} {max_num}")