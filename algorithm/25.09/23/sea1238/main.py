import sys
sys.stdin = open('input (7).txt','r')


from collections import deque

T = 10
for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    child = [[] for _ in range(100+1)]

    for i in range(int(n/2)):
        x, y = nums[i*2], nums[i*2+1]
        child[x].append(y)

    visited = set()
    p_list = deque()
    new_p_list = deque()
    new_p_list.append(m)
    visited.add(m)

    while True:
        p_list = new_p_list
        new_p_list = deque()

        for next_child in p_list:
            for val in child[next_child]:
                if val not in visited:
                    visited.add(val)
                    new_p_list.append(val)

        if not new_p_list:
            break

    print(f"#{tc} {max(p_list)}")




