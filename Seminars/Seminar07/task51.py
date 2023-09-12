# Задача №51. 
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.

# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, object):
    if len(object) == 0:
        return True
    someValues = list(map(characteristic, object))
    first = someValues[0]

#    print(f"someValues = {someValues}")

    for value in someValues:
        if first != value:
            return False
    return True
#    return len(set(map(characteristic, object)))

values = [7, 2, 15, 11]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")


