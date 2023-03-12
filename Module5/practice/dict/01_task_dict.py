# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# item_count - количество товара который планирует купить клиент
# Считая,что курс доллара равен dollar_rate
# Вычислите стоимость покупки в долларах

# Информация о товаре
item = {"name": "Кроссовки", "price": 7540.5, "currency": "rub"}
# Количество товаров
item_count = 8
# Курс доллара
dollar_rate = 74.12
final_price = 0
i = 0
while i <= item_count:
    final_price += item["price"]/dollar_rate
    i += 1
print(final_price)
