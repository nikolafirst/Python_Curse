# Задача №15.
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

max = 0

total_summ = int(input("Введите количество арбузов -> "))
amount = [random.randint(1, 10) for _ in range(total_summ)]
# print(str(amount).strip("[]"))   раскоммитить, будет выполняться печать списка что бы наглядно посмотреть min и max

for i in amount:
    if i > max:
        max = i
        i += 1
min = min(amount)

print(f"Арбуз по тяжелее равен  {max} кг", "\n" f"Арбуз по легче равен {min} кг")

"""
def find_max_min_mass(count_watermelon):
    max, min = 1, 21
    for i in range(count_watermelon):
        mass = random.randrange(1, 20)
        print(mass, end=" ")
        if max < mass:
            max = mass
        if min > mass:
            min = mass
    print(end="\n")
    return min, max


count_watermelon = int(input("Введите количество арбузов: "))
print(find_max_min_mass(count_watermelon))
"""
