import sys
sys.stdin = open('input (2).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    v, e, n1, n2 = map(int, input().split())
    nums = list(map(int, input().split()))
    parent = [[] for _ in range(v+1)]
    child = [[] for _ in range(v+1)]

    for i in range(0, e * 2, 2):
        x = nums[i]
        y = nums[i+1]
        parent[y].append(x)
        child[x].append(y)

    parent_list = [[] for _ in range(2)]
    for x in range(2):  # 조상 탐색
        dq = deque()
        if x == 0:
            dq.append(n1)
        if x == 1:
            dq.append(n2)

        while dq:
            xx = dq.popleft()
            if parent[xx]:
                parent_list[x].append(parent[xx][0])
                dq.append(parent[xx][0])

    ans = 0
    for i in parent_list[0]:  # 가장 가까운 공통 조상
        for j in parent_list[1]:
            if i == j and ans == 0:
                ans = i
                break

    ans_cnt = 1
    dq = deque()
    dq.append(ans)
    while dq:
        x = dq.popleft()
        for i in child[x]:
            dq.append(i)
            ans_cnt += 1

    print(f"#{tc} {ans} {ans_cnt}")


