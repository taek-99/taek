food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for i in range (3):
    if food_list[i]['이름'] == '토마토':
        food_list[i]['종류'] = '과일'
    if food_list[i]['이름'] == '자장면':
        print ("자장면엔 고춧가루지")

    print (f"{food_list[i]['이름']}은/는 {food_list[i]['종류']} (이)다.")

print (food_list)


i = 0
while i < 3:
    if food_list[i]['이름'] == '토마토':
        food_list[i]['종류'] = '과일'
    if food_list[i]['이름'] == '자장면':
        print ("자장면엔 고춧가루지")
    print (f"{food_list[i]['이름']}은/는 {food_list[i]['종류']} (이)다.")
    i += 1

print (food_list)