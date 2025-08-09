T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split()))for _ in range (n)]
    
    stair_pos = []
    people = []
    cnt = 0
    men_num = 1
    for i in range (n): # 계단 위치 찾기 & 인원 위치
        for j in range (n):
            if board[i][j] == 1:
                people.append ((i, j))
            if board[i][j] > 1:
                stair_pos.append([i, j, board[i][j]])
    
    outter = []
    for i, j in people: # 인원별 계단 a, b까지의 거리
        a_stair = (abs(i - stair_pos[0][0]) + abs(j - stair_pos[0][1]) + 1)
        b_stair = (abs(i - stair_pos[1][0]) + abs(j - stair_pos[1][1]) + 1)
        outter.append ((a_stair, b_stair))
    
    
    stair_1 = []
    stair_2 = []
    def sol(arr, stair):
        if not arr:
            return 0
            
        arr.sort()
        total = max(arr[:3]) + stair
        
        for i in range(3, len(arr)):
            total = max(total, max((arr[i-3]+ stair), arr[i])+stair)
    
        return total
    
    best = 10**9
    for i in range (2 ** len(people)):
        men_num = i
        arr1 = []
        arr2 = []
        for j in range (len(people)):      
            if men_num >> j & 1 == 1:
                arr1.append (outter[j][0])
            else:
                arr2.append (outter[j][1])
    
        best = min(best, max (sol(arr1, stair_pos[0][2]), sol(arr2, stair_pos[1][2])))
    
    print (f"#{tc} {best}")

    # QED 이명재
        