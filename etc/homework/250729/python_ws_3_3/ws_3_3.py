number_of_book = 100

def decrease_book(num):
    global number_of_book
    number_of_book -= num

    print (f"남은 책의 수 : {number_of_book}")


def rental_book(name, number):

    decrease_book(number)

    book = {}
    book['name'] = name
    book['number'] = number

    return book

result = rental_book('홍길동', 3)
print (f"{result['name']}님이 {result['number']}권의 책을 대여하였습니다.")