"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, last):
    items = [first, second, last]
    items.remove(min(items))
    return sum(items)


a, b, c = int(input("Число (a): ")), int(input("Число (b): ")), int(input("Число (c): "))

print(f"Сумма двух наибольших чисел - {my_func(a, b, c)}")
