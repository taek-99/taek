import sys
sys.stdin = open('input (7).txt', 'r')

for tc in range (1, 11):
    t = int(input())
    board = [list(map(int, input().split()))for _ in range (100)]
    visited = [[False] * 100 for _ in range (100)]

    def visited_re(): # visited 초기화
        for ii in range (100):
            for jj in range (100):
                if board[ii][jj] == 1:
                    visited[ii][jj] = True

    def sol(x, y):
        global cnt

        if x == 99:
            return
        ly = y - 1
        ry = y + 1
        visited[x][y] = False

        if 0 <= ly < 100 and visited[x][ly]:
            cnt += 1
            sol (x, ly)
        elif 0 <= ry < 100 and visited[x][ry]:
            cnt += 1
            sol (x, ry)
        else:
            nx = x + 1
            sol (nx, y)


    min_cnt = 100*100
    ans = 0
    for i in range (100):
        if board[0][i] == 1:
            cnt = 0
            visited_re()
            sol (0, i)
        if cnt < min_cnt:
            min_cnt = cnt
            ans = i

    print (f"#{tc} {ans}")
