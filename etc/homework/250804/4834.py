T = int(input())
 
for tc in range (T):
    n = int(input())
    num = str(input())
     
    ans_list = [0] * 10
     
    for i in num:
        a = int(i)
        ans_list[a] +=1
     
    ans_max = 0
    for index, value in enumerate(ans_list):
        if value >= ans_max:
            ans_index = index
            ans_max = value
     
    print (f"#{tc+1} {ans_index} {ans_max}")