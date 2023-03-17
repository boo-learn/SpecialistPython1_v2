# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
for num, item in enumerate(items, 1):
    print(f"{num}. {item['name']}")
# 2. Выведите цену самого дешевого товара
prices = []
for item in items:
    prices.append(float(item["price"]))

prices.sort()
print(prices[0])
