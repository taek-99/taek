T = int(input())
 
for tc in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
     
    ans_list = []
    for i in range(0, N-M+1):
        ans_list.append(sum(num_list[i:i+M]))
     
    print (f"#{tc+1} {max(ans_list)-min(ans_list)}")