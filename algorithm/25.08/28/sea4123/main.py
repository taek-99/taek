import sys
sys.stdin = open('sample_input (12).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    card = list(map(int, input().split()))
    nums = list(map(int, input().split()))


    def dfs(idx, num):
        global min_num, max_num

        if idx == n-1:
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        if card[0] > 0:
            card[0] -= 1
            dfs(idx+1, num+nums[idx+1])
            card[0] += 1

        if card[1] > 0:
            card[1] -= 1
            dfs(idx+1, num-nums[idx+1])
            card[1] += 1

        if card[2] > 0:
            card[2] -= 1
            dfs(idx+1, num*nums[idx+1])
            card[2] += 1

        if card[3] > 0:
            card[3] -= 1
            dfs(idx+1, int(num/nums[idx+1]))
            card[3] += 1


    max_num = -10 ** 10
    min_num = 10 ** 10
    dfs(0, nums[0])

    print(f"#{tc} {max_num-min_num}")