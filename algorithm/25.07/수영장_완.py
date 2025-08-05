test_case = int(input())

for ii in range (test_case):
    num = int(input())
    board = [list(map(int, input().split())) for i in range (num)]
    rail = [[0]*num for i in range (num)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 해당자리 주변값 +1, 현재 자리도 1초 지났기 때문에 +1
    def sol(x, y, z):
        
        rail[x][y] = z + 1
        for k in range (4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < num and 0 <= ny < num and rail[nx][ny] == 0:
                rail[nx][ny] = z + 1
    
    # 장애물 -999, 소용돌이 -500
    for i in range (num):
        for j in range (num):
            if board[i][j] == 1:
                rail[i][j] = -999
            elif board[i][j] == 2:
                rail[i][j] = -500
    
    
    # 시작점은 세팅/ 소용돌이 위치 저장
    rail[start[0]][start[1]] = 1
    sol (start[0], start[1], 1)
    ans = 1
    swl = []
    for i in range (num):
        for j in range (num):
            if rail[i][j] == -500:
                swl.append ([i, j])
    
    # 길 찾기
    while True:
        for i in range (num):
            for j in range (num):
                if rail[i][j] == ans:
                    sol (i, j, ans)
    
    # 소용돌이 on, off
        for i, j in swl:
            if rail[i][j] == -500 and ans % 3 == 2:
                rail[i][j] = 0
            elif rail[i][j] == 0:
                rail[i][j] = -500
                
        ans += 1
        if rail[end[0]][end[1]] != 0:
            print (f"#{ii+1} {ans-1}")
            break
        elif ans > num*num and rail[end[0]][end[1]] == 0:
            print (f"#{ii+1} -1")
            break