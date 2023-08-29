# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5
import random

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
n = 0
for i in range(len(list_1)):
    if (k - list_1[i]) < k - n and k - list_1[i] > 0:
        n = i
print(list_1[n])


# print(list_1)
