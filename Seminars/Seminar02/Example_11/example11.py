# Задача №11.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Введите число: "))


def fib(n):
    n1 = 0
    n2 = 1
    res = 0
    count = 2
    while res < n:
        res = n1 + n2
        n1 = n2
        n2 = res
        count += 1
    if res == n:
        return count
    else:
        return -1


print(fib(n))

# def search_possition_number_in_Fibbonachi(number):
#     num_fib = [0,1]
#     while number > num_fib[-1] :
#         new_num_fib = num_fib[-1]+num_fib[-2]
#         num_fib.append(new_num_fib)
#     if num_fib[-1] == number:
#         return len(num_fib)
#     return -1



# try: 
#     number = int(input("Введите число: "))

#     print(f"Позиция числа {number} в последовательности Фиббоначи ---> {search_possition_number_in_Fibbonachi(number)}")
# except:
#     print("Ввели неверные данные")
