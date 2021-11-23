# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
#   “название”: [“компьютер”, “принтер”, “сканер”],
#   “цена”: [20000, 6000, 2000],
#   “количество”: [5, 2, 7],
#   “ед”: [“шт.”]
# }

product_list = []
product_structure = {
    "Название": str,
    "Цена": int,
    "Количество": int,
    "Единица измерения": str,
}
product_number = 1

while True:
    should_add_new_product = input(f"Товаров в каталоге - {len(product_list)}, добавить? [n - для отмены] ")

    if should_add_new_product.lower() == 'n':
        break
    else:
        try:
            product_info = {}

            for property_name, property_type in product_structure.items():
                user_input = input(f"{property_name} товара: ")
                product_info[property_name] = property_type(user_input)

            product_list.append((product_number, product_info))
            product_number += 1
        except ValueError:
            print("Неверный формат данных")

product_analytics = {}

for key in product_structure.keys():
    item_list = []
    for product in product_list:
        item_list.append(product[1][key])

    product_analytics[key] = item_list

print(product_analytics if len(product_list) > 0 else 'Каталог пуст')
