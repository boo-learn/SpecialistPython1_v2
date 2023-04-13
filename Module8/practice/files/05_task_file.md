## "Улучшенный кассовый аппарат"

### Задание
Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров. \
Файл [data/items_sold.txt](data/items_sold.txt) - продажи всех товаров за день. \
Каждая строка файла - покупка одного покупателя.

Узнайте:
1. Какова общая выручка магазина
2. Какова выручка магазина по каждому типу товаров
3. Какой тип товара был продан на самую большую сумму
4. Сколько различных типов товаров было продано за день

### Формат входных данных

Дан текстовый файл. На каждой строке записана информация о проданных товарах в формате:

**тип_товара:цена**, например **fruits:45.10**

Все проданные товары разделены одним или более пробелами.

### Формат выходных данных

Вывести:
1. Какова общая выручка магазина
2. Какова выручка магазина по каждому типу товаров
3. Какой тип товара был продан на самую большую сумму. Если таких несколько, вывести любой.
4. Сколько различных типов товаров было продано за день

### Решение задачи

path = "items_sold.txt"

names = []
prices = []
max_price = 0

with open(path, "r", encoding="utf-8") as f:

    for line in f:
        temp_string = line.split()
        for el in temp_string:
            temp_name = el.split(":")[0]
            temp_price = float(el.split(":")[1])
            if temp_name not in names:
                # новый вид товаров
                names.append(temp_name)
                prices.append(temp_price)
                if temp_price > max_price:
                    max_price = temp_price
            else:
                # увеличиваем цену известного вида товара
                prices[names.index(temp_name)] += temp_price
                if prices[names.index(temp_name)] > max_price:
                    max_price = prices[names.index(temp_name)]

    print()
    # print(names)
    # print(prices)
    # print()

    print("Товаров продано на общую сумму: ", sum(prices))
    print()
    for num, el in enumerate(names):
        print(f"Товаров '{el}' на общую сумму {prices[num]:.2f}")
    print()
    print(f"Большего всего получено ({max_price:.2f}) от продажи '{names[prices.index(max_price)]}'")
    print()
    print(f"Всего в магазине {num + 1} видов товаров")

---
