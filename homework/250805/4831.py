from collections import deque
 
T = int(input())
 
for tc in range(T):
    k, n, m = map(int, input().split())
    cha_num = list(map(int, input().split()))
     
    start = 0
    ans = 0
    end = 0
    while True:
         
        cha_pos = 0
        for i in range(start+1, start+1+k):
            if i in cha_num:
               cha_pos = i
            if i == n:
                end = 1
                break
     
        if end:
            break
        else:
            if cha_pos:
                ans += 1
                start = cha_pos
            else:
                ans = 0
                break
     
    print (f"#{tc+1} {ans}")
        