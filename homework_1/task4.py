# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

number = int(input('Введите число: '))
result = 0

while number:
    current = number % 10
    number = number // 10
    result = current if current > result else result

print('Самое большое число: ', result)
