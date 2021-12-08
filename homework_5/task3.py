"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('task3_workers.txt') as file:
    pairs = [line.replace('\n', '').split(' ') for line in file]

total_salary = 0

print('Сотрудники с ЗП менее 20 000:')
for k, v in pairs:

    if float(v) < 20000:
        print(f'- {k}')

    total_salary += float(v)

average_salary = total_salary / len(pairs)

print(f"Средняя ЗП: {round(average_salary, 2)}")