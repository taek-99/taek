import sys
sys.stdin = open('sample_input (20).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    max_ans = 0
    min_ans = sum(num[0:m])

    for i in range(n-m+1):
        ans = 0
        for j in range(i, i+m):
            ans += num[j]
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans

    print (tc)
    print (max_ans - min_ans)