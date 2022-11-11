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
for i, item in enumerate(items):
    print(f"{i+1}. {item['name']}")
prices = [float(item["price"]) for item in items]
cheapest = min(prices)
print(f"Цена самого дешевого товара: {cheapest}")
