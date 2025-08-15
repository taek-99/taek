T = int(input())

for tc in range(1, T+1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    honey_price = [[0] * (n-m+1) for _ in range(n)]
    
        
    def hoeny_dfs(honey_list):
        if sum(honey_list) <= c: # 꿀통을 다 더해도 c보다 작으면 가지치기
            return sum(x*x for x in honey_list)
        
        best = 0
        def dfs(idx, total, sq):
            nonlocal best
            if total > c:
                return
        
            if idx == m:
                if sq > best:
                    best = sq
                return 
        
            hh = honey_list[idx]
            dfs (idx+1, total + hh, sq + hh*hh)
            dfs (idx+1, total, sq)
    
        dfs (0, 0, 0)
        return best
    
    for i in range(n): # 각 구역 가격 금액 책정
        for j in range(n-m+1):
            best = 0
            honey_list = board[i][j:j+m]
            honey_price[i][j] = hoeny_dfs(honey_list)
    
    
    max_price = 0
    for i in range(n):
        for j in range(n-m+1):
            work_man_a = honey_price[i][j]
    
            for ii in range(i, n):
                for jj in range(n-m+1):
                    work_man_b = 0
                    if ii == i:
                        if jj > j+m:
                            work_man_b = honey_price[ii][jj]
                    else:
                        work_man_b = honey_price[ii][jj]
    
                    max_price = max(max_price, (work_man_a+work_man_b))
    
    print (f"#{tc} {max_price}")
    





    