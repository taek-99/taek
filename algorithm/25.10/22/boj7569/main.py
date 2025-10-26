

k = 100
n = int(input())
board = [[False] * k for _ in range(k)]

ans = 0
for _ in range(n):
    st_pos, ed_pos = map(int, input().split())

    for i in range(ed_pos, ed_pos+10):
        for j in range(st_pos, st_pos+10):
            if not board[i][j]:
                ans += 1
                board[i][j] = True

print (ans)