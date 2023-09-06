# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

from random import randint

print("Заполняем массив элементами арифметической прогрессии!!!")
# print("\n")


def arithmetic_progression(a1, d, n):
    arithmetic_progression = [0] * n
    for i in range(n):
        arithmetic_progression[i] = a1 + i * d
        return arithmetic_progression


a1 = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))  # насколько я понял подразумевается количество элементов в массиве

print(arithmetic_progression(a1, d, n))

# инициализация массива
# arithmetic_progression = [0] * n

# заполнение массива элементами арифметической прогрессии
# for i in range(n):
#     arithmetic_progression[i] = a1 + i * d

# вывод массива
# print("Массив арифметической прогрессии:", arithmetic_progression)
