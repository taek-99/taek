from collections import deque
 
T = int(input())
 
for tc in range(T):
    n = int(input())
    num = sorted(map(int, input().split()))
    dq = deque(num)
     
    ans_list = []
     
    for i in range(10):
        if i % 2 == 0:
            ans_list.append(dq.pop())
        else:
            ans_list.append(dq.popleft())
 
    ans = " ".join(map(str,ans_list))
    print (f"#{tc+1} {ans}")