"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def form_user_data(
    first_name: str = None,
    last_name: str = None,
    birth_year: int = None,
    city: str = None,
    phone: str = None,
    email: str = None
):
    return f"{first_name} {last_name} {birth_year} г.р., город - {city}, тел: {phone}, e-mail: {email}"


user_first_name = input("Имя:")
user_last_name = input("Фамилия:")
user_birth_year = int(input("Год рождения: "))
user_city = input("Город: ")
user_email = input("Email: ")
user_phone = input("Номер телефона: ")

print(
    form_user_data(first_name=user_first_name, last_name=user_last_name,
                   birth_year=user_birth_year, city=user_city, email=user_email,
                   phone=user_phone)
)
