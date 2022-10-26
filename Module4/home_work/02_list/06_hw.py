# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

brands = {items[0]["brand"]}
for item in items:
    brands.add(item["brand"])
print(f"Товары на складе представлены брэндами: {brands}")

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

print("На складе самый дорогой товар брэнда(ов): ")

highest_price = 0
highest_brands = []
for item in items:
    if float(item["price"]) > highest_price:
        highest_price = float(item["price"])
for item in items:
    if item["price"] == highest_price:
        highest_brands.append(item["brand"])
print(f"На складе самый дорогой товар брэнда(ов): {highest_brands}")
