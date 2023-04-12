# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
...
# 2. Выведите цену самого дешевого товара
...

min_price = float(items[0]["price"])
for i, _ in enumerate(items):
    print(f"{i}.", items[i]["name"])
    if float(items[i]["price"]) < min_price:
        min_price = float(items[i]["price"])

print("Цена самого дешёвого товара: ", min_price)
