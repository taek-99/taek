# 아래 함수를 수정하시오.
def add_item_to_dict(my_dict, a, b):
    
    new_dict = dict.copy(my_dict)
    new_dict[a] = b

    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
