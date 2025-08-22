import sys
sys.stdin = open('input (1).txt','r')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    prime = [2, 3, 5, 7, 11]
    ans = [0] * 5

    for pr in range(5):
        while not num % prime[pr]:
            num = int(num / prime[pr])
            ans[pr] += 1
            if num == 0:
                break

    a = ' '.join(map(str, ans))
    print (f"#{tc} {a}")