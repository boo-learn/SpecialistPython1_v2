# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
for i, item in enumerate(items, 1):
    str_name = item["name"]
    print(f"{i}. {str_name}")
# 2. Выведите цену самого дешевого товара
for i, item in enumerate(items, 1):
    if i == 1:
        min_price = item["price"]
    elif float(item["price"]) <= float(min_price):
        min_price = item["price"]

print("\n", min_price)
