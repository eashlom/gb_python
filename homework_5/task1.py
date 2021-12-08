"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

strings = []

while True:
    with open('task1_strings.txt', 'a+') as file:
        string = input("Введите строку: ")

        if not string:
            break

        file.write(f"{string}\n")