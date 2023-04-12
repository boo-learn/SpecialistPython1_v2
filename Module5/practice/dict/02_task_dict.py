# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
for i, item in enumerate(items):
    print(f"{i+1}. {item['name']}")

# 2. Выведите цену самого дешевого товара
min_price = min(float(item['price']) for item in items)
print(f"Цена самого дешевого товара: {min_price} руб.")
...
