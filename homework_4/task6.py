"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

# скрипт A
print("Iterator A")
start_iterator = 3

for el in count(start_iterator):
    if el > 10:
        break

    print(el)

# скрипт B
print("Iterator B")
cycling_list = [6, 16, 24, 17]
max_iterations = 20
iteration_count = 0

for el in cycle(cycling_list):
    print(el)
    iteration_count += 1

    if iteration_count >= max_iterations:
        break
