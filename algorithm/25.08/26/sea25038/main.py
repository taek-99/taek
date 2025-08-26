import sys
sys.stdin = open('taek/algorithm/25.08/26/sea25038/input1.txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]

    child = [[] for _ in range(n+1)]

    for i in range(len(num)):
        x = i +1
        for j in range(1, len(num[i])):
            child[x].append(num[i][j])

    ans_list = set()
    tt = 0
    while True:
        visited = False
        for i in range(1, len(child)):  # 선수과목 완료한 과목 확인
            if not child[i] and i not in ans_list:
                ans_list.add(i)
                visited = True
        
        for i in ans_list:  # 삭제해야할 목록 확인
            for j in range(1, n+1):
                if i in child[j]:
                    child[j].remove(i)
                    visited = True

        tt += 1
        if len(ans_list) == n:
            print (f"#{tc} {tt}")
            break

        if not visited:
            print (f"#{tc} -1")
            break

        