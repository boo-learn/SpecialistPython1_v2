# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# item_count - количество товара который планирует купить клиент
# Считая,что курс доллара равен dollar_rate
# Вычислите стоимость покупки в долларах

# Информация о товаре
item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub"}
# Количество товаров
item_count = 8
# Курс доллара
dollar_rate = 74.12

item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub"}
item_count = 8
dollar_rate = 74.12

price_usd = round(float(item["price"]) / dollar_rate, 2)

total_cost_usd = price_usd * item_count

print(f"Стоимость {item_count} товаров '{item['name']}' в долларах: {total_cost_usd}")
