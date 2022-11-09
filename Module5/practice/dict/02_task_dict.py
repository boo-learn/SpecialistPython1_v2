# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]
min_price = float(-1)
for i, item in enumerate(items, 1):
    print("{}. {}".format(str(i), item["name"]))
    if min_price > float(item["price"]) or min_price < float(0):
        min_price = float(item["price"])
print("Мин. цена:",min_price)
