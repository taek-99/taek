n = int(input())

board = [list(input()) for _ in range (n)]
visited = [[False] * n for _ in range (n)]

for i in range (n):
    for j in range (n):
        if board[i][j] == "Y":
            visited[i][j] = True
            

# 겹치는 친구 확인
for i in range (n):
    for j in range (n):
        if board[i][j] == "Y":
            for k in range (n):
                if board[j][k] == "Y" and k != i:
                    visited[i][k] = True


# 각 인원별 친구수 확인
fri = []
for i in range (n):
    f_cnt = 0
    for j in range (n):
        if visited[i][j] == True:
            f_cnt += 1
    fri.append(f_cnt)

print (max(fri))    