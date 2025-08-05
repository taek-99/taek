import sys
input = sys.stdin.readline

t = int(input())

n = []
for i in range (t):
    n.append(int(input()))


for i in n:
    a = 0
    b = 1
    c = 0
    if i == 0:
        print (1, 0)
    else:
        for j in range (1, i):
            c = a + b 
            a = b
            b = c 
        print (a, b)   