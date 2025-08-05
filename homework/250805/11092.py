T = int(input())
 
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
     
    # 최솟값
    for index, value in (enumerate(num)):
        if value == min(num):
            min_num = index
            break
             
    # 최댓값
    for index, value in reversed(list(enumerate(num))):
        if value == max(num):
            max_num = index
            break
             
    print (f"#{tc+1} {abs(max_num-min_num)}")