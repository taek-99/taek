for tc in range(1, 11):
    v, e = map(int, input().split())
    nums = list(map(int, input().split()))
    board = [[False] * (v+1) for _ in range(v+1)]
    
    for k in range(0, e*2, 2):
        x = nums[0+k]
        y = nums[1+k]
        board[y][x] = True
    
    
    ans_list = []
    while True:
        for i in range (1, v+1):
            if all(not num for num in board[i]):
                if not i in ans_list:
                    ans_list.append(i)
                    for j in range (1, v+1):
                        if board[j][i]:
                            board[j][i] = False
        if len(ans_list) == v:
            break
            
    ans = ' '.join(map(str, ans_list))
    print (f"#{tc} {ans}")
                