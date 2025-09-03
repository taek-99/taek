T = int(input())
 
for tc in range(T):
    str1 = str(input())
    str2 = str(input())
     
    if str1 in str2:
        ans = 1
    else:
        ans = 0
     
    print (f"#{tc+1} {ans}")