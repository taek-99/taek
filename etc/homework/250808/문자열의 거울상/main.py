import sys

sys.stdin = open('input (7).txt','r')


T = int(input())
for tc in range (1, T+1):
    str_list = input()
    str_dict = {
        'b' : 'd',
        'd' : 'b',
        'q' : 'p',
        'p' : 'q',
    }

    ans = ""
    for i in str_list[::-1]:
        ans += str_dict[i]

    print (f"#{tc} {ans}")