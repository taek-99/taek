n, m = map(int, input().split())
nums = []

for i in range(1, n+1):
    nums.append(i)


def perm(selected):
    if len(selected) == m+1:
        a = ' '.join(map(str, selected[1:]))
        print (a)
        return

    for i in range(1, len(nums)+1):
        select_i = i
        if selected[-1] <= select_i:
            perm(selected + [select_i])


perm([0])