from collections import deque
import sys

input = sys.stdin.readline

L = int(input())
qd = list(map(int, input().split()))
nnn = list(map(int, input().split()))
n = int(input())
num = deque(map(int, input().split()))


ans = []
for j in range (L-1, -1, -1):
    if qd[j] == 0:
        ans.append(nnn[j])
    if len(ans) == n:
        break
        
if len(ans) != n :
    for i in num:
        ans.append(i)
        if len(ans) == n:
            break
            
 
print (*ans)