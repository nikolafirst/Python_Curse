# Задача №9.
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Input: 5
# Output: 120

n = int(input("Введите целое не отрицатильное число: "))
while n <= 0:
    print("Введите число больше нуля!!!")
    n = int(input("Введите целое не отрицатильное число: "))
N = 1
while n > 1:
    N *= n
    n -= 1
print(N)
