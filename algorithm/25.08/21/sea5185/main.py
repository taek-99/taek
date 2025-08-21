import sys
sys.stdin = open('sample_input (2).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(str, input().split())
    nums = list(k)

    ans = []
    for i in nums:
        a = int(i, 16)
        for j in range(3, -1, -1):
            ans.append(a//2**j)
            a = a % 2**j

    b = ''.join(map(str, ans))
    print (f"#{tc} {b}")

