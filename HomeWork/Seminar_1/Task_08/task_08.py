# Задача 8

#  Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

first_slices = int(input("Введите первое значение: "))
second_slices = int(input("Введите второе значение: "))
total = int(input("Введите количество долек: "))


if (first_slices * second_slices) // total == 1:
    print("yes")
else:
    print("no")