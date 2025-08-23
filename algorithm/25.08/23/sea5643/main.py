import sys
sys.stdin = open('taek/algorithm/25.08/23/sea5643/sample_input (31).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    m = int(input())
    parents = [[] for _ in range(n+1)]
    child = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        parents[x].append(y)
        child[y].append(x)

    print (parents)
    print (child)
    ans = 0
    for i in range(1, n+1):
        people = set()
        dq = deque()
        people.add(i)

        dq.append(i)
        while dq:  # 부모 노드 찾기
            a = dq.popleft()
            for x in parents[a]:
                if x not in people:
                    people.add(x)
                    dq.append(x)
        
        dq.append(i)
        while dq:  # 자식 노드 찾기
            a = dq.popleft()
            for x in child[a]:
                if x not in people:
                    people.add(x)
                    dq.append(x)


        if len(people) == n:
            ans += 1

    print (f"#{tc} {ans}")