# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def find_index_in_range(arr, min_value, max_value):
    index = []
    for i, num in enumerate(arr):
        if num >= min_value and num <= max_value:
            index.append(i)
    return index

arr = [1, 5, 88, 100, 2, -4]
min_value = 33
max_value = 200

index = find_index_in_range(arr, min_value, max_value)

print("Ответ:", index)