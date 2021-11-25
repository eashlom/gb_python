"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

** Подсказка:**
попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_simple(x, y):
    return x ** y


def my_func_harder(x, y):
    result = x

    if y > 0:
        for _ in range(1, y):
            result *= x
    else:
        for _ in range(1, y, -1):
            result /= x

    return result


user_x, user_y = float(input("Первое число: ")), int(input("Второе число: "))

print(my_func_simple(user_x, user_y))
print(my_func_harder(user_x, user_y))