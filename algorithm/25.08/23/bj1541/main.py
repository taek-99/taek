expr = input().strip()

blocks = expr.split('-')
sums = []

for block in blocks:
    if block == '':
        sums.append(0)
    else:
        parts = block.split('+')
        s = 0
        for p in parts:
            if p:
                s += int(p)
        sums.append(s)

answer = sums[0]
for v in sums[1:]:
    answer -= v

print(answer)
