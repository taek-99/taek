test_case = int(input())

for j in range (test_case):
    money = int(input())
    board = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = []
    
    for i in board:
        ans.append (money // i)
        money = money % i

    print (f"#{j+1}")
    print (*ans)