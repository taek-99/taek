T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    def sol (line):
        used = [False] * n
        for i in range(n-1):
            if line[i] == line[i+1]: #다음꺼랑 높이 같으면 패스
                continue
            elif line[i] + 1 == line[i+1]: #오르막
                for j in range(i, i - m, -1):
                    if j < 0 or line[j] != line[i] or used[j]:
                        return False
                    used[j] = True
            elif line[i] - 1 == line[i+1]: # 내리막
                for j in range(i + 1, i + 1 + m):
                    if j >= n or line[j] != line[i+1] or used[j]:
                        return False
                    used[j] = True
            else:
                return False
        return True
    

    
    ans = 0
    for row in board:
        if sol(row):
            ans += 1
    for col in zip(*board):
        if sol(list(col)):
            ans += 1
            
    print (f"#{tc} {ans}")