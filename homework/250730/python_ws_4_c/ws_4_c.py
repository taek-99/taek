matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.

max_len = 0
for i in matrix:
    max_len += 1
print (max_len)

number = 0
for i in range(max_len):
    temporay_len = 0
    for j in matrix[i]:
        temporay_len += 1
    if temporay_len < 5:
        print (f"{matrix[i]} 리스트는 {temporay_len}개 만큼 요소를 가지고 있습니다.")


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print (f"matrix의 {x}, {y} 번째 요소의 값은 {matrix[x][y]} 입니다.")