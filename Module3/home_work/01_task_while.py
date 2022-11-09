cost = float(input("Введите стоимость товара: "))
n = int(input("Введите кол-во единиц товара: "))
i = 1
while i < n + 1:
    print(i, i * cost, "рублей")
    i += 1
