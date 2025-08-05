T = int(input())

for t in range (T):
    n = int(input())
    arr = [[0]*n for i in range (n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    a = 0
    x = 0
    y = 0
    
    for i in range (1, n*n + 1):
        arr[x][y] = i
        nx = x + dx[a]
        ny = y + dy[a]
       
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:    
            x, y = nx, ny
        else:
            a += 1
            if a == 4:
                a = 0
            x += dx[a]
            y += dy[a]
    

    print (f"#{t+1}")
    for i in arr:
        print (' '.join(map(str, i)))
        