import sys
sys.stdin = open('sample_input (22).txt','r')

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    n = len(str1)
    m = len(str2)

    complete = 0
    for i in range(m):
        if str1 == str2[i:i+n]:
            complete = 1

    print(f"#{tc} {complete}")