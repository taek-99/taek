import sys
sys.stdin = open('sample_input (28).txt','r')

## 이건 실패 ===============================
from itertools import combinations, permutations

T = int(input())


n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for val in permutations(nums, n):
    bit_num = 1
    print (val, ":========")
    for i in range(2**n):
        bit_num = i
        right_chu = []
        left_chu = []
        for j in range(n):
            if bit_num >> j & 1 == 1:
                if sum(left_chu) > sum(right_chu):
                    right_chu.append(val[j])
            else:
                left_chu.append(val[j])

        if sum(left_chu) >= sum(right_chu):
            print (left_chu, right_chu)
            cnt += 1

print (cnt)
