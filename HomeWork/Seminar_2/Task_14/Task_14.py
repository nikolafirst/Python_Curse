# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


number = int(input("Введите число: "))
a =[]
count = 0
b = 0
while b < number:
    a.append(count)
    count += 1
    b = 2**count
print(*a)


