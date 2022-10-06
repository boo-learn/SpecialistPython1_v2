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

# TODO: your code here

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

print("На складе самый дорогой товар брэнда(ов): ")


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

max_number_of_goods = 0
for item in brands_items.items():
    if item[1] > max_number_of_goods:
        brands = [item[0]]
        max_number_of_goods = item[1]
    elif item[1] == max_number_of_goods:
        brands.append(item[0])
print(f"На складе больше всего товаров брэнда(ов): {', '.join(brands)}")

max_price = 0
brands = []
for item in brands_price.items():
    if item[1] > max_price:
        brands = [item[0]]
        max_price = item[1]
    elif item[1] == max_price:
        brands.append(item[0])
print(f"На складе самый дорогой товар брэнда(ов): {', '.join(brands)}")
