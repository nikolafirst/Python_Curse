# Задача 1
# HARD по желанию Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

from decimal import Decimal

num = Decimal(input("Введите число: "))
# n = (",")
count = 0
if num == 0:
    count = 1
else:
    num = abs(num)
    while num > 0:
        count += 1
        num //= 10

print("Количество цифр в числе:", count)
