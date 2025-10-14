
T = int(input())

for tc in range(1, T+1):
    n, l = map(int, input().split())
    hambuger = [list(map(int, input().split())) for _ in range(n)]


    def dfs(idx, taste, cal):
        global max_taste
        
        if cal > l:  # 현재 칼로리가 최대 칼로리보다 넘어가면
            return 
        max_taste = max(max_taste, taste)

        if idx == n:  # 마지막 재료에 다다르면 종료
            return 

        dfs(idx+1, taste+hambuger[idx][0], cal+hambuger[idx][1])
        dfs(idx+1, taste, cal)


    max_taste = 0
    dfs (0, 0, 0)  # 인덱스 번호, 맛, 칼로리

    print (f"#{tc} {max_taste}")