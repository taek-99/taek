import sys
sys.stdin = open('sample_input (24).txt','r')

from collections import deque

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))


    def merge(left, right):
        global  cnt

        result = []

        if left[-1] > right[-1]:
            cnt += 1

        left = deque(left)
        right = deque(right)

        while left and right:
            if left[0] < right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())

        result.extend(left)
        result.extend(right)

        return result


    def merge_sort(arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)


    cnt = 0
    nums = merge_sort(nums)
    print(f"#{tc} {nums[n//2]} {cnt}")