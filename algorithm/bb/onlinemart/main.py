import sys
from solution import init, sell, closeSale, discount, show
CMD_INIT = 100
CMD_SELL = 200
CMD_CLOSE_SALE = 300
CMD_DISCOUNT = 400
CMD_SHOW = 500


def run1():
    global  xxx
    Q = int(input())
    okay = False
    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
<<<<<<< HEAD
        xxx += 1
        print (xxx,cmd, "==================")
=======
        print (cmd , "HHHHHHHHHHHHHHHHHHHH")
>>>>>>> 52ffc52bed26a23a3921d0289ecdc29000175de2
        if cmd == CMD_INIT:
            init()
            okay = True
        elif cmd == CMD_SELL:
            mID = int(next(input_iter))
            mCategory = int(next(input_iter))
            mCompany = int(next(input_iter))
            mPrice = int(next(input_iter))
            ret = sell(mID, mCategory, mCompany, mPrice)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
            print (ret)
        elif cmd == CMD_CLOSE_SALE:
            mID = int(next(input_iter))
            ret = closeSale(mID)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
            print (ret)
        elif cmd == CMD_DISCOUNT:
            mCategory = int(next(input_iter))
            mCompany = int(next(input_iter))
            mAmount = int(next(input_iter))
            ret = discount(mCategory, mCompany, mAmount)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
            print (ans)
        elif cmd == CMD_SHOW:
            mHow = int(next(input_iter))
            mCode = int(next(input_iter))
            res = show(mHow, mCode)
            cnt = int(next(input_iter))
            if res.cnt != cnt:
                okay = False
            for i in range(cnt):
                ans = int(next(input_iter))
                if res.IDs[i] != ans:
                    okay = False
        else:
            okay = False
    return okay


<<<<<<< HEAD
sys.stdin = open('sample_input (36).txt','r')
=======
sys.stdin = open('sample_input (36).txt', 'r')
>>>>>>> 52ffc52bed26a23a3921d0289ecdc29000175de2

T, MARK = map(int, input().split())

xxx = 0
for tc in range(1, 2):
    score = MARK if run1() else 0
    print("#%d %d" % (tc, score), flush = True)
