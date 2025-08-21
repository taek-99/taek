import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    ans = True
    for i in range(0, n):
        if m >> i & 1 != 1:
            ans = False
    if ans:
        print (f"#{tc} ON")
    else:
        print(f"#{tc} OFF")