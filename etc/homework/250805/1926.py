from collections import deque
 
n = int(input())
 
num = []
for i in range (1, n+1):
    num.append(str(i))    
 
 
ans_list =[]
 
for i in num:
    count_num = 0
    if "3" in i:
        count_num += i.count("3")
    if "6" in i:
        count_num += i.count("6")
    if "9" in i:
        count_num += i.count("9")
     
    if count_num:
        ans_list.append("-"*count_num)
    else:
        ans_list.append(str(i))
 
print (*ans_list)