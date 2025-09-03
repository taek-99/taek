number_of_people = 100


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    many_user = {
        'name' : name,
        'age' : age,
        'address' : address
    }
    
    return many_user


def rental_book(info):
    pass
    decrease_book(info)


# 고객 나이를 10으로 나눈 몫을 대여할 책의 수
def decrease_book(data):
    pass
    increase_user (data // 10)


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in name:
    print(f"{i}님 환영합니다!")

print(list(map(create_user,name, age, address)))

