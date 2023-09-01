# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

a = int(input("Enter (a): "))
b = int(input("Enter (b): "))


def f(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b - 1)


result = f(a, b)
print(result)


# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a