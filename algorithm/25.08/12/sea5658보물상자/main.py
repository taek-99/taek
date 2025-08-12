from collections import deque
T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    treasure = deque(input())
    
    lenght = n // 4
    
    num_list = set([])
    for _ in range(12):
        ans_str = "0x"
        for i in treasure:
            ans_str += i
            if len(ans_str) == 2 + lenght:
                num_list.add(int(ans_str, 16))
                ans_str = "0x"
            
        treasure.rotate(1)
        
    ans_list = sorted(list(num_list), reverse=True)
    print (f"#{tc} {ans_list[k-1]}")