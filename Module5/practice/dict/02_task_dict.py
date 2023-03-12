# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
min_price = float(items[0]["price"])
for i in range(len(items)):
    print(i+1, items[i]["name"])
    if min_price > float(items[i]["price"]):
        min_price = float(items[i]["price"])
# 2. Выведите цену самого дешевого товара
print(min_price)
