import sys
sys.stdin = open ('sample_input (12).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    tree = [0 for _ in range(n+1)]

    for _ in range(m):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(n, 1, -1):
        tree[i//2] += tree[i]

    print(f"#{tc} {tree[l]}")