import sys
sys.stdin = open('input (18).txt','r')

for tc in range(1, 11):
    n = int(input())
    arr = input()

    num_rank={
        "("  : 0,
        "+" : 1,
        "-" : 1,
        "*" : 2,
        "/" : 2,
    }

    num_list = []
    operator_list = []

    for i in arr:
        if i.isnumeric():
            num_list.append(i)
        elif i =='(':
            operator_list.append(i)

        elif i ==')':
            top_token = operator_list.pop()
            while top_token != '(':
                num_list.append(top_token)
                pop_token = operator_list.pop()
        else:
            while operator_list and num_rank[operator_list[-1]] >= num_rank[i]:
                num_list.append(operator_list.pop())
            operator_list.append(i)

    while operator_list:
        num_list.append(operator_list.pop())

    a = ''.join(num_list)

    stack = []
    result = 0
    for token in a:
        if token.isnumeric():
            stack.append(int(token))
        else:
            oop2 = stack.pop()
            oop1 = stack.pop()
            if token == "+":
                result = oop1 + oop2
            if token == "-":
                result = oop1 - oop2
            if token == "*":
                result = oop1 * oop2
            if token == "/":
                result = oop1 / oop2
            stack.append(result)

    print (f"#{tc} {stack.pop()}")