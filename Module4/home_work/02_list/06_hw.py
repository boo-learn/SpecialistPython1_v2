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

brands = []
for item in items:
    if item["brand"] not in brands:
        brands.append(item["brand"])
print()
print("Товары на складе представлены брэндами: ", brands)
print()

amount = []
i = 0
for i in range(len(brands)):
    amount.append(0)
    i += 1
for item in items:
    amount[brands.index(item["brand"])] += 1
for i in range(len(brands)):
    print(f"Товаров бренда '{brands[i]}': {amount[i]} штук(а/и)")
print()

# Определяем максимальный объём среди брендов
max_amount = 0
for i in range(len(amount)):
    if amount[i] > max_amount:
        max_amount = amount[i]
# Составляем список брендов с максимальным количеством товаров
max_amount_brands = []
for i in range(len(amount)):
    if amount[i] == max_amount:
        max_amount_brands.append(brands[i])
print("На складе больше всего товаров брэнда(ов): ", max_amount_brands)
print()

max_price = 0
max_price_brand = ""
for item in items:
    if item["price"] > max_price:
        max_price = item["price"]
        max_price_brand = item["brand"]
print(f"На складе самый дорогой товар - брэнда '{max_price_brand}', цена одного из товаров которого составила {max_price}")
