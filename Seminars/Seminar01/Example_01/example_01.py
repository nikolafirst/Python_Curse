# Задача №1.


# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.


n = int(input("Введите сколько машина за день проехжает километров:\n "))
m = int(input("Введите сколько машина должна проехать километров:\n "))
d = m // n
ost = m % n

print(d + bool(ost))
