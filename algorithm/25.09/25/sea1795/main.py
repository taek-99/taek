import sys
sys.stdin = open('input (9).txt','r')


import heapq

T = int(input())

n, m, x = map(int, input().split())
adj_list = {i: {} for i in range(1, n+1)}

for _ in range(m):
    u, w, val = map(int, input().split())
    adj_list[u][w] = val

max_num = 0
print(adj_list)
for i in range(1, n+1):
    ans = 0
    for j in [i, x]:
        heap_list = {ii: float('inf') for ii in range(1, n + 1)}
        heap_list[j] = 0
        min_heap = []
        heapq.heappush(min_heap, [0, j])

        print(heap_list)
        while min_heap:
            v, x = heapq.heappop(min_heap)

            if heap_list[x] < v:
                continue

            for next_pos, weight in adj_list[v].items():
                distance = weight + v
                if distance < heap_list[next_pos]:
                    heap_list = distance
                    heapq.heappush(min_heap, [distance, next_pos])

                if next_pos == j:
                    ans = heap_list[j]
                    break
            if ans:
                break


print (max_num)



