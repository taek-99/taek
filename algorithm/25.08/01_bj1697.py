# 이건 안되는 거임 절대 안됨
# gpt의 도움을 받았는데도 조건이 너무 많아서 프로그램 짜기에 불편
# 시간초과 무조건 남 

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N, M = map(int, input().split())


if N >= M:
    print(N - M)
    sys.exit(0)

ans = M - N

cur_pos = N
pre_pos = N
cnt = 0
max_cnt = 100000
max_pos = 100000
best = [100000] * (max_pos+1)

def sol (cur_pos, cnt):
    global max_cnt

    # cur_pos가 0보다 작아지거나 최적의 수보다 높으면 리턴.
    if cur_pos < 0 or cur_pos > max_pos:
        return

    if cnt >= max_cnt:
        return
    
    if cnt >= best[cur_pos]:
        return
    best[cur_pos] = cnt
    
    # 정답에 도달 했을 때
    if cur_pos == M:    
        max_cnt = cnt
        return
        
    if cur_pos * 2 == M or cur_pos + 1 == M or cur_pos - 1 == M:
        if cnt + 1 < max_cnt:
            max_cnt = cnt + 1
        return
        
    if cur_pos > M:
        cand = cnt + (cur_pos - M)
        if cand < max_cnt:
            max_cnt = cand
        return
        
    if cur_pos > 0:
        nx = cur_pos * 2
        if nx <= 100000:
            sol(cur_pos * 2, cnt + 1)

    sol (cur_pos + 1, cnt + 1)
    sol (cur_pos - 1, cnt + 1)

sol(cur_pos, cnt)

print (max_cnt)


# ================================
## GPT 형님이 알려준 bfs버전 이게 맞다.

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

# N이 K보다 크거나 같으면 뒤로만 가면 됨
if N >= K:
    print(N - K)
    sys.exit(0)

MAX = 100000
dist = [-1] * (MAX + 1)   # 방문 및 시간(초) 기록
q = deque([N])
dist[N] = 0

while q:
    x = q.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
