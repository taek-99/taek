test_case = int(input())

for k in range (test_case):
    n = int(input())
    board = list(map(int, input().split()))
    aa = board
    sum_max = 0
        
    





    
   """ for jj in range (n):
        aaa = 0
        bbb = 0
        for i in range (n):
            if aaa <= aa[i]:
                aaa = aa[i]
                bbb = i 
    
        for i in range (bbb):
            if aa[i] > 0:
                sum_max += aaa - aa[i]
                aa[i] = -999
        aa[bbb] = -999"""
            
        
    print(f"#{k+1} {sum_max}")
    

    
