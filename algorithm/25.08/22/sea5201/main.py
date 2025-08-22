import sys
sys.stdin = open('sample_input (7).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))


    weight.sort(reverse=True)
    ans = 0
    for tt in truck:
        for i in range(len(weight)):
            if tt >= weight[i]:
                ans += weight[i]
                del weight[i]
                break


    print (f"#{tc} {ans}")