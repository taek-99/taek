import sys
sys.stdin = open('sample_input (6).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    honey_price = [[0] * (n-m+1) for _ in range(n)]


    def honey_dfs(idx, total, sq):
        global max_honey

        if total > c:
            return

        if idx == m:
            max_honey = max(max_honey, sq)
            return

        hh = honey_list[idx]
        honey_dfs (idx+1, total + hh, sq + hh*hh)
        honey_dfs(idx + 1, total, sq)


    for i in range(n):
        for j in range(n - m + 1):
            max_honey = 0
            honey_list = board[i][j:j+m]
            if sum(honey_list) <= c:
                honey_price[i][j] = sum(x * x for x in honey_list)
            else:
                honey_dfs(0, 0, 0)
                honey_price[i][j] = max_honey

    max_price = 0
    for i in range(n):
        for j in range(n-m+1):
            a_work_man = honey_price[i][j]

            for ii in range(n):
                for jj in range(n-m+1):
                    b_work_man = 0
                    if ii == i:
                        if jj > j+m:
                            b_work_man = honey_price[ii][jj]
                    else:
                        b_work_man = honey_price[ii][jj]

                    max_price = max(max_price, (a_work_man + b_work_man))

    print (f"#{tc} {max_price}")


