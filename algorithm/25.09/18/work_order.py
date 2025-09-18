import sys
sys.stdin = open('sample_input (13).txt','r')


from collections import defaultdict

v,e = map(int, input().split())
edged = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(e):
    graph[edged[2*i]].append(edged[2*i+1])

print (graph)

visited = [False] * (v+1)
result = []


def dfs(x):
    visited[x] = True

    for adj in graph[x]:
        if not visited[adj]:
            dfs(adj)

    result.append(x)


for i in range(1, v+1):
    if not visited[i]:
        dfs(i)

print (*result[::-1])