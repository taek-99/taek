n = 5
p = [0] * (n+1)

def make_set(x):
    p[x] = x

# def find_set(x):
#     if x == p[x]:
#         return x
#     return (find_set(p[x]))

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        py = px
    else:
        px = py