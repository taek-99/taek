T = int(input())

for k in range (T):
    tc, n = map(str, input().split())
    num = list(map(str, input().split()))

    num_list = []
    for i in num:
        if i == "ZRO":
            num_list.append(0)
        elif i == "ONE":
            num_list.append(1)
        elif i == "TWO":
            num_list.append(2)
        elif i == "THR":
            num_list.append(3)
        elif i == "FOR":
            num_list.append(4)
        elif i == "FIV":
            num_list.append(5)
        elif i == "SIX":
            num_list.append(6)
        elif i == "SVN":
            num_list.append(7)
        elif i == "EGT":
            num_list.append(8)
        elif i == "NIN":
            num_list.append(9)
    
    num_list.sort()
    
    ans_list = []
    for i in num_list:
        if i == 0:
            ans_list.append("ZRO")
        elif i == 1:
            ans_list.append("ONE")
        elif i == 2:
            ans_list.append("TWO")
        elif i == 3:
            ans_list.append("THR")
        elif i == 4:
            ans_list.append("FOR")
        elif i == 5:
            ans_list.append("FIV")
        elif i == 6:
            ans_list.append("SIX")
        elif i == 7:
            ans_list.append("SVN")
        elif i == 8:
            ans_list.append("EGT")
        elif i == 9:
            ans_list.append("NIN")
    print (tc)
    print (*ans_list)
            