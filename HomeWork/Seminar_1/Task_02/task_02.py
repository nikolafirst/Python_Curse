# Задача 2:

# Найдите сумму цифр трехзначного числа

random_number = int(input("Введите трехзначное число:\t"))
if random_number < 0 or random_number > 1000:
    print("Введено не трехзначное число")

c = random_number // 100
print(c)
b = (random_number // 10) % 10
print(b)
a = random_number % 10
print(a)

total = a + b + c
print(f"Сумма введенного числа равна:\t {total}")
