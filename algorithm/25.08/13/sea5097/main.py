import sys
from collections import deque
sys.dtdin = open('5097_input.txt','r')


T = int(input())
n, m = map(int, input().split())
num_list = deque(map(str, input().split()))

print (num_list)
for i in range (m):
    print (i)
    num_list.rotate(1)

print (num_list[0])