import sys
sys.stdin = open('sample_input (13).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    card = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_num = -10**10
    min_num = 10**10


    def dfs(idx, score, card):
        global max_num, min_num

        if idx == n-1:
            max_num = max(max_num, score)
            min_num = min(min_num, score)
            return

        if card[0] > 0:
            card[0] -= 1
            dfs(idx+1, score+nums[idx+1], card)
            card[0] += 1

        if card[1] > 0:
            card[1] -= 1
            dfs(idx+1, score-nums[idx+1], card)
            card[1] += 1

        if card[2] > 0:
            card[2] -= 1
            dfs(idx+1, score*nums[idx+1], card)
            card[2] += 1

        if card[3] > 0:
            card[3] -= 1
            dfs(idx+1, int(score/nums[idx+1]), card)
            card[3] += 1


    dfs(0, nums[0], card)

    print(f"#{tc} {max_num-min_num}")