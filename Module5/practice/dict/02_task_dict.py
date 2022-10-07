# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

n = 0
min_cost = float(items[0]["price"])
for item in items:
    print(n, ":", item["name"]," ", item["price"])
    if float(item["price"]) < min_cost:
        min_cost = float(item["price"])
    n += 1
print("самый дешевый товар:", min_cost)
