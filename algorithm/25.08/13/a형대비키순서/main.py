## 14:50
## 15:14
 
from collections import deque
 
T = int(input())
 
for tc in range(1, T+1):
    n = int(input())
    m = int(input())
    board = []
    for _ in range(m):
        board.append(list(map(int, input().split())))
 
    parent = [[] for _ in range(n+1)]
    child = [[] for _ in range(n+1)]
 
    for x, y in board:
        parent[x].append(y)
        child[y].append(x)
 
    ans_list = []
    for i in range(1, n+1):
        family_list = set()
        parent_list = deque(parent[i][:])
        child_list = deque(child[i][:])
        family_list.add(i)
 
        while parent_list: #부모 찾기
            q = parent_list.popleft()
 
            if q not in family_list:
                for i in parent[q]:
                    parent_list.append(i)
                family_list.add(q)
 
        while child_list: #자식 찾기
            q = child_list.popleft()
            if q not in family_list:
                for i in child[q]:
                    child_list.append(i)
                family_list.add(q)
 
        if len(family_list) == n:
            ans_list.append(i)
 
    print (f"#{tc} {len(ans_list)}")