# 아래 함수를 수정하시오.
def get_keys_from_dict(my_dict):
    a = []
    for i in my_dict.keys():
      a.append(i)

    return a

def get_all_keys_from_dict(dictionary):
    b = []
    for i, j in dictionary.items():
       b.append(i)
       if isinstance (j, dict):
          b.extend(get_all_keys_from_dict(j))
    return b


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
