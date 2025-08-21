import sys
sys.stdin = open('sample_input (2).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = float(input())

    ans = ""
    nn = n
    for i in range(1, 13):
        if n >= 2 ** -i:
            n = n - 2 ** -i
            ans += "1"
        else:
            ans += "0"
        if n <= 0:
            print(f"#{tc} {ans}")
            break
    else:
        print(f"#{tc} overflow")