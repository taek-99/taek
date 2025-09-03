for tc in range (10):
    T = int(input())
    num = [list(map(int, input().split())) for _ in range(100)]
     
    ans_list = []
     
    for i in range (100):
        ans_list.append(sum(num[i])) # 가로
        ans = 0 
        for j in range (100):
            ans += num[j][i] # 세로
        ans_list.append(ans)
     
    # 대각선 1
    ans = 0 
    for i in range (100):
        for j in range (100):
            if i == j:
                ans += num[i][j]
    ans_list.append(ans)
     
    # 대각선 2
    ans = 0 
    x = 4
    y = 0
    cnt = 0
    for i in range (100):
        for j in range (100):
            if i == y and j == x:
                ans += num[i][j]
                x -= 1
                y += 1
    ans_list.append(ans)
     
    print (f"#{T} {max(ans_list)}")