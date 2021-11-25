"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return "Ошибка деления"


user_dividend = int(input("Введите первое число: "))
user_divisor = int(input("Введите второе число: "))

print(divide(user_dividend, user_divisor))
