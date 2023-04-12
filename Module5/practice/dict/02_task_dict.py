# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
for n, item in enumerate(items, 1):
    print(n, item["name"])
...
# 2. Выведите цену самого дешевого товара
mincost = float(items[0]["price"])
price = 0

for elem in items:
    price = float(elem["price"])
    if price < mincost:
        mincost = price

print(mincost)

