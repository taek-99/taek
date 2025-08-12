from collections import deque

T = int(input())
for tc in range(1,T+1):
    v, e, a, b = map(int, input().split())
    nums = list(map(int, input().split()))
    parents = [0] * (v+1)
    children = [[] for _ in range(v+1)] 

    for i in range(0, e*2, 2):
        x = nums[i]
        y = nums[i+1]
        parents[y] = x
        children[x].append(y)
        
        
    a_ans = []
    b_ans = []

    #조상노드 찾기
    while a:
        if parents[a]:
            a_ans.append(parents[a])
            a = parents[a]
        else:
            break
            
    while b:
        if parents[b]:
            b_ans.append(parents[b])
            b = parents[b]
        else:
            break

    ans = 0 #가까운 조상 찾기
    for i in a_ans:
        for j in b_ans:
            if i == j:
                ans = i
        if ans > 0:
            break


    ans_list = deque([])
    ans_list.append(ans)
    cnt = 0
    
    while ans_list:
        node = ans_list.popleft()
        for i in children[node]:
            ans_list.append(i)
            cnt += 1
        
    
    print (f"#{tc} {ans} {cnt+1}")