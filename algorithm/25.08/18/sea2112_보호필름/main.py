T = int(input())

for tc in range(1, T+1):
    d, w, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(d)]

    zero_row = [0] * w
    one_row = [1] * w
    best = k
    
    if k == 1:
        print (f"#{tc} 0")
        continue

    def test_pass(bd):
        for c in range(w):
            cnt = 1
            ok = False
            for r in range(1, d):
                if bd[r][c] == bd[r-1][c]:
                    cnt += 1
                    if cnt >= k:
                        ok = True
                        break
                else:
                    cnt = 1
            if not ok:
                return False
        return True

    def dfs(r, used):
        global best

        if used >= best:
            return

        if test_pass(board):
            best = used
            return

        if r == d:
            return

        saved = board[r]

        is_zero = all(x == 0 for x in saved)
        is_one = all(x == 1 for x in saved)

        dfs(r+1, used)

        if not is_zero:
            board[r] = zero_row
            dfs (r+1, used+1)
            
        if not is_one:
            board[r] = one_row
            dfs (r+1, used+1)
            
        board[r] = saved
        
    
    dfs (0, 0)

    print (f"#{tc} {best}")