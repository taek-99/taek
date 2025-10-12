import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
start_v = int(input())

adj_list = {i : {} for i in range(n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    adj_list[u][v] = min(w, adj_list[u].get(v, w))

INF = float("INF")
heap_list = [INF] * (n+1)
heap_list[start_v] = 0

min_heap = []
heapq.heappush(min_heap, (0, start_v))

while min_heap:
    val, pos = heapq.heappop(min_heap)

    if heap_list[pos] < val:
        continue

    for next_pos, weight in adj_list[pos].items():
        distance = val + weight
        if distance < heap_list[next_pos]:
            heap_list[next_pos] = distance
            heapq.heappush(min_heap, (distance, next_pos))

for idx in range(1, n+1):
    if heap_list[idx] == INF:
        print ("INF")
    else:
        print (heap_list[idx])