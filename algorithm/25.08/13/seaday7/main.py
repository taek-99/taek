from collections import deque

for tc in range(10):
    T = int(input())
    num_list = deque(map(int, input().split()))

    k = len(num_list)
    cnt = 0
    while True:
        cnt += 1
        num = num_list.popleft()
        num = num - cnt
        if num < 0:
            num = 0
        num_list.append(num)

        if cnt == 5:
            cnt = 0

        if num == 0:
            ans = ' '.join(map(str, list(num_list)))
            print(f"#{T} {ans}")
            break

