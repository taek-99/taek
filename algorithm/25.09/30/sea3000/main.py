import sys
sys.stdin = open('sample_input (22).txt','r')


import heapq

MOD = 20171109
T = int(input())
for tc in range(1, T + 1):
    N, A = map(int, input().split())

    # lower: 최대힙(파이썬은 최소힙이므로 음수로 저장), upper: 최소힙
    lower, upper = [], []

    def push_num(x):
        # 1) lower에 우선 넣음 (중앙값은 lower 루트가 되게 유지)
        if not lower or x <= -lower[0]:
            heapq.heappush(lower, -x)
        else:
            heapq.heappush(upper, x)
        # 2) 균형 맞추기: len(lower) == len(upper) 또는 1개 더 많게
        if len(lower) < len(upper):
            heapq.heappush(lower, -heapq.heappop(upper))
        elif len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))

    # 초기값 삽입
    push_num(A)

    ans = 0
    for _ in range(N):
        x, y = map(int, input().split())
        push_num(x)
        push_num(y)
        median = -lower[0]
        ans = (ans + median) % MOD

    print(f"#{tc} {ans}")
