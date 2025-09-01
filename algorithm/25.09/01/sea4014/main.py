import sys
sys.stdin = open('taek/algorithm/25.09/01/sea4014/sample_input (40).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int ,input().split()))for _ in range(n)]


    def sol(bd, used):
        for x in range(n-1):  
            if abs(bd[x] - bd[x+1]) > 1:
                return False

            if bd[x] == bd[x+1] + 1:  # 내리막
                if x + k >= n:
                    return False
                
                for y in range(x+1, x+k+1):
                    if bd[y] != bd[x+1] or used[y]:
                        return False
                    else:
                        used[y] = True

            if bd[x] == bd[x+1] - 1:  # 오르막
                if x - (k-1) < 0:
                    return False

                for y in range(x, x-k, -1):
                    if bd[y] != bd[x] or used[y]:
                        return False
                    else:
                        used[y] = True
        return True
                

    ans = 0
    for i in range(n):  # 가로
        bd = board[i]
        used = [False] * n
        if sol(bd, used):
            ans += 1
        
    bd = list(zip(*board))
    for i in range(n):
        used = [False] * n
        if sol(list(bd[i]), used):
            ans += 1

    print (f"#{tc} {ans}")