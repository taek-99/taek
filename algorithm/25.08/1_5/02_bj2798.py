import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans_list = []


for j in combinations(nums, 3):
    ans = sum(j)
    if ans <= m:
        ans_list.append(ans)
    if ans == m:
        break

print (max(ans_list))