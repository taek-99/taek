## 14:17
## 14:58

import sys
sys.stdin = open('input (23).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    parents = [[] for _ in range(n+1)]

    for i in range(n):
        for j in range(len(nums[i])):
            if j > 0:
                parents[i+1].append(nums[i][j])

    ans = 0
    visited = set()
    while True:
        move = False
        for i in range(1, n+1):
            if not parents[i] and i not in visited:
                visited.add(i)
                move = True

        for i in visited:
            for j in range(1, n+1):
                if i in parents[j]:
                    parents[j].remove(i)
                    move = True

        ans += 1
        if len(visited) == n:
            break

        if not move:
            ans = -1
            break

    print (f"#{tc} {ans}")