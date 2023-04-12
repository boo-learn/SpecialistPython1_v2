# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
num = 1
for item in items:
    print(f"{num}) {item['name']}")
    num += 1
# 2. Выведите цену самого дешевого товара
cheap_price = float(items[1]["price"])
for item in items:
    if float(item["price"]) < cheap_price:
        cheap_price = float(item["price"])
print(cheap_price)
