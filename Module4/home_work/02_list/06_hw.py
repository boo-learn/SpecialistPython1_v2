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

brands_items = {}
brands_price = {}
for item in items:
    if item['brand'] in brands_items:
        brands_items[item['brand']] += 1
        brands_price[item['brand']] = max(brands_price[item['brand']], item['price'])
    else:
        brands_items[item['brand']] = 1
        brands_price[item['brand']] = item['price']
print(f"Товары на складе представлены брэндами: {', '.join(brands_items.keys())}")

max_number_of_goods = max(brands_items.values())
brands = [brand for brand, number_of_goods in brands_items.items() if number_of_goods == max_number_of_goods]
print(f"На складе больше всего товаров брэнда(ов): {', '.join(brands)}")

max_price = max(brands_price.values())
brands = [brand for brand, price in brands_price.items() if price == max_price]
print(f"На складе самый дорогой товар брэнда(ов): {', '.join(brands)}")
