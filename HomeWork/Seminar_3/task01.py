# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

import random

# ls = int(input("Введите длину списка: "))
list_1 = [random.randint(1, 20) for _ in range(15)]
k = 3
n = 0
for i in range(len(list_1)):
    if i == k:
        n += 1
        i += 1

# print(str(list_1).strip('[]'))
print(list_1)
print(n)
