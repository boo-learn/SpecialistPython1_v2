# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

min_price = float(items[0]['price'])
print(f"### {'name':<10} {'price':<10} currency")
for i, obj in enumerate(items, 1):
    print(f"{i:>3} {obj['name']:<10} {obj['price']:>10} {obj['currency']}")
    if float(obj['price']) < min_price: min_price = float(obj['price'])

print("min_price: ", min_price)
