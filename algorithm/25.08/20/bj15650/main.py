n, m = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append (i)


def combi(arr, x):
    result = []
    if x == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combi(arr[i + 1:], x-1):
            result.append([elem] + rest)
    return result

ans = combi(nums, m)

for i in ans:
    a = ' '.join(map(str, i))
    print (a)