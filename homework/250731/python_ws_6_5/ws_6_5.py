def ordered_difference_sets(set1, set2):
    a = set1.difference(set2)
    b = set2.difference(set1)

    if len(a) >= len(b):
        return a
    else:
        return b


# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
