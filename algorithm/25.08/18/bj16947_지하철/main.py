from collections import deque

n = int(input())
nums = [list(map(int, input().split()))for _ in range(n)]
node_list = [[] for _ in range(n+1)]
node_num = [0] * (n+1)

ans_list = []

for i, v in nums:
    node_list[i].append(v)
    node_list[v].append(i)
    node_num[i] += 1
    node_num[v] += 1
    

print (node_list)
print (node_num)
dq = deque()
for i in range (1, n+1):
    if node_num[i] == 1:
        dq.append(i)

while dq: # 잎사귀 제거
    x = dq.popleft()
    node_num[x] = 0
    for v in node_list[x]:
        if node_num[v] > 0:
            node_num[v] -= 1
            if node_num[v] == 1:
                dq.append(v)

print (node_num)
on_cycle = [False] * (n+1)
dq = deque()
for i in range(1, n+1): # 순환인 노드 True로 확인
    if node_num[i]:
        on_cycle[i] = True

print ("on_cycle", on_cycle)
dist = [-1] * (n+1)
dq = deque()
for i in range(1, n+1):
    if on_cycle[i]:
        dist[i] = 0
        dq.append(i)


print ("dist", dist)
while dq:
    x = dq.popleft()
    for v in node_list[x]:
        if dist[v] == -1:
            dist[v] = dist[x] + 1
            dq.append(v)

print (*dist[1:])
