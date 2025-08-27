import sys
sys.stdin = open('taek/algorithm/25.08/26/sea2477/sample_input (32).txt','r')
from collections import deque


T = int(input())

for tc in range(1, T+1):
    n, m, k, a, b = map(int, input().split())
    rec_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    customor = list(map(int, input().split()))

    customor_visit_list = [[] for _ in range(k)]
    rec_wait_list = deque()
    repair_wait_list = deque()

    rec_desk = [0] * n
    repair_desk = [0] * m

    rec_man = [-1] * n
    repair_man = [-1] * m

    tt = 0
    end_man = 0

    while True:
        for i in range(k):  # 접수 창구에 도착
            if tt == customor[i]:
                rec_wait_list.append(i)

        for j in range(n):  # 접수 창구
            if not rec_desk[j] and rec_wait_list:
                rec_desk[j] = rec_time[j]
                rec_man[j] = rec_wait_list.popleft()
                customor_visit_list[rec_man[j]].append(j)
        
        for j in range(m):  # 수리 창구
            if not repair_desk[j] and repair_wait_list:
                repair_desk[j] = repair_time[j]
                repair_man[j] = repair_wait_list.popleft()
                customor_visit_list[repair_man[j]].append(j)

        for i in range(n):  # 접수 창구 시간가는중
            if rec_desk[i] > 0:
                rec_desk[i] -= 1
                if not rec_desk[i]:
                    repair_wait_list.append(rec_man[i])
                    rec_man[i] = -1

        for i in range(m):  # 수리 창구 시간가는중
            if repair_desk[i] > 0:
                repair_desk[i] -= 1
                if repair_desk[i] == 0:
                    repair_man[i] = -1
                    end_man += 1

        tt += 1
        if end_man == k:
            break


    ans = 0
    for idx, val in enumerate(customor_visit_list):
        if (val[0]+1, val[1]+1) == (a, b):
            ans += idx+1

    if ans == 0:
        print(f"#{tc} -1")
    else:
        print (f"#{tc} {ans}")