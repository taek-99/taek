import sys
sys.stdin = open('input (10).txt','r')

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())

    if str1 == str1[::-1]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")