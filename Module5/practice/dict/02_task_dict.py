# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
low_price = float(items[0]["price"])
num = 1
for i in items:
    print(num, i["name"])
    if float(i["price"]) < low_price:
        low_price = float(i["price"])
    num += 1

# 2. Выведите цену самого дешевого товара
print('Самый дешевый: ', low_price)
