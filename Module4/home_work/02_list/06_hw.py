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

brands = []
for item in items:
    found = False
    for brand in brands:
        if brand["name"] == item["brand"]:
            found = True
            brand["brand_goods_count"] += 1
            if item["price"] > brand["brand_goods_max_price"]:
                brand["brand_goods_max_price"] = item["price"]
    if not found:
        brands.append(dict(name=item["brand"], brand_goods_count=1, brand_goods_max_price=item["price"]))

print("Товары на складе представлены брэндами: ", end="")
first = True
for brand in brands:
    if first:
        first = False
    else:
        print(", ", end="")
    print(brand["name"], end="")
print(".")

brands.sort(key=lambda x: x["brand_goods_count"], reverse=True)
print("На складе больше всего товаров брэнда(ов): ", end="")
first = True
brand_goods_count = brands[0]["brand_goods_count"]
for brand in brands:
    if brand["brand_goods_count"] == brand_goods_count:
        if first:
            first = False
        else:
            print(", ", end="")
        print(brand["name"], end="")
print(".")

brands.sort(key=lambda x: x["brand_goods_max_price"], reverse=True)
print("На складе самый дорогой товар брэнда(ов): ", end="")
first = True
brand_goods_max_price = brands[0]["brand_goods_max_price"]
for brand in brands:
    if brand["brand_goods_max_price"] == brand_goods_max_price:
        if first:
            first = False
        else:
            print(", ", end="")
        print(brand["name"], end="")
print(".")
