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
        "price": 25000
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
brands = {}
max_brand_name = ""
max_brand_cnt = 0
max_cost_name = ""
max_cost = 0
for item in items:
    if item["brand"] in brands:
        brands[item["brand"]] += 1
    else:
        brands[item["brand"]] = 1
    if max_brand_cnt < brands[item["brand"]]:
        max_brand_cnt = brands[item["brand"]]
        max_brand_name = item["brand"]
    if max_cost < item["price"]:
        max_cost = item["price"]
        max_cost_name = item["brand"]

print(f"Товары на складе представлены брэндами: {list(brands.keys())}")
print("На складе больше всего товаров брэнда(ов): {}, {} шт".format(max_brand_name, max_brand_cnt))
print("На складе самый дорогой товар брэнда(ов): %s, %s" % (max_cost_name, max_cost))
