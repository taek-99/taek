import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
n_list = deque(sorted(list(map(int, input().split()))))
M = int(input())
m_list = list(map(int, input().split()))
cnt_list = {key: 0 for key in m_list}
mq_list = deque(sorted(m_list))

m_q = [1]
n_q = [1]

while mq_list:
    m_q = mq_list.popleft()
    while n_list:
        n_q = n_list.popleft()
        if n_q == m_q:
            cnt_list[m_q] += 1
        if n_q > m_q:
            n_list.appendleft(n_q)
            break
            
ans_list = [cnt_list[i] for i in m_list]

print (*ans_list)