# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
cheep_price = float(items[0]['price'])
for i, item in enumerate(items):
    print(f"{i + 1} {item['name']}")
    if float(item['price']) < cheep_price:
        cheep_price = float(item['price'])
# 2. Выведите цену самого дешевого товара
print(f"Цена самого дешевого товара {cheep_price:.2f}")
