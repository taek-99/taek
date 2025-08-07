import sys
sys.stdin = open('input (7).txt', 'r')

for tc in range (1, 11):
    dumb = int(input())
    num_list = list(map(int, input().split()))

    for i in range (dumb):
        max_index = num_list.index(max(num_list))
        min_index = num_list.index(min(num_list))
        num_list[max_index] -= 1
        num_list[min_index] += 1
    print (f"#{tc} {max(num_list) - min(num_list)}")