n, m = map(int, input().split())
nums = []

for i in range(1, n+1):
    nums.append(i)


def perm(selected, remain):
    if len(selected) == m:
        a = ' '.join(map(str, selected))
        print (a)

    for i in range(len(remain)):
        select_i = remain[i]
        remain_list = remain[:i] + remain[i+1:]
        perm(selected + [select_i], remain_list)


perm([], nums)