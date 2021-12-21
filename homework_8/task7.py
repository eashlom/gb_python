"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0:
            return f'{self.b}i'
        elif self.b == 0:
            return str(self.a)
        else:
            b = '+' + str(self.b) if self.b >= 0 else self.b
            return f'{self.a}{b}i'

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return ComplexNumber(a, b)


num1 = ComplexNumber(1, -1)
num2 = ComplexNumber(3, 6)
print(num1 + num2)
print(num1 * num2)
