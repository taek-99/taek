T = int(input())
 
for tc in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    a = max(num_list)
    ans_list = [[0] * n for _ in range(a)]
    for i in range(a):
        for j in range(n):
            if num_list[j] > 0:
                ans_list[i][j] = 1
                num_list[j] -= 1
      
    max_ans = 0
     
    for i in ans_list:
        cnt = 0
        for j in range(n):
            if i[j]:
                for k in range(j+1, n):
                    if not i[k]:
                        cnt += 1
                break
        if cnt > max_ans:
            max_ans = cnt
     
    print (f"#{tc+1} {max_ans}")