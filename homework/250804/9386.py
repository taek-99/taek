T = int(input())
 
for tc in range(T):
    N = int(input())
    num = str(input())
     
     
    cnt = 0
    ans_cnt = []
    for i in num:
        if i == "1": # 1이 나오면 카운팅
            cnt +=1
        if i == "0": # 0이 나오면 초기화
            cnt = 0
        ans_cnt.append(cnt)
     
    print (f"#{tc+1} {max(ans_cnt)}")