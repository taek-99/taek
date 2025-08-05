import math

n = int(input())
m = (int(math.log2(n))+2)


board = [list(map(int, input().split()))for _ in range (n)]
visited = [[False] * n for _ in range (n)]


w_paper = 0
b_paper = 0

k = n * 2

for ii in range (1, m): #2 대신 m
    k = k // 2
    for i in range (0, n, k):
        for j in range (0, n, k):
            if not visited[i][j]:
                if all(board[x][y] == 1 for x in range(i, i+k) for y in range(j, j+k)):
                    for a in range (i, i+k):
                        for b in range (j, j+k):
                            visited[a][b] = True
                    b_paper +=1
                if all(board[x][y] == 0 for x in range(i, i+k) for y in range(j, j+k)):
                    for a in range (i, i+k):
                        for b in range (j, j+k):
                            visited[a][b] = True
                    w_paper +=1

print (w_paper)
print (b_paper)

