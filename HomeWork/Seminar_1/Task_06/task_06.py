# Задача 6

#  Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета

number_ticket = int(input("Введите шестизначный номер вашего билета: "))
# print(f"{number_ticket}")

firstHalf_ticket = number_ticket // 1000

c = firstHalf_ticket // 100
b = (firstHalf_ticket // 10) % 10
a = firstHalf_ticket % 10
summ_firstHalf_ticket = a + b + c

secondHalf_ticket = number_ticket % 1000

q = secondHalf_ticket // 100
w = (secondHalf_ticket // 10) % 10
e = secondHalf_ticket % 10
summ_secondHalf_ticket = q + w + e

if summ_firstHalf_ticket==summ_secondHalf_ticket:
    print("- УРА ,вам достался счастливый билет - ")
else:
    print(" - Увы, вам не выпал счастливый билет - ")
