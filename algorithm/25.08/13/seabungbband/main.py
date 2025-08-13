test_case = int(input())

for jj in range(test_case):
    n, m, k = map(int, input().split())
    person = sorted(list(map(int, input().split())))

    ans = "Possible"

    for i in range(n):
        if i + 1 > person[i] // m * k:
            ans = "Impossible"
            break

    print(f"#{jj + 1} {ans}")