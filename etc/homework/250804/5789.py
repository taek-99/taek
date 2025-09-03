T = int(input())
 
for tc in range(T):
    n, q = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(q)]
     
    num_list = [0] * n
     
    for i in range(len(num)):
        for j in range(num[i][0], num[i][1]+1):
            num_list[j-1] = i + 1
 
    ans = ' '.join (map(str, num_list))
    print (f"#{tc+1} {ans}")