# Посчитайте количество согласных букв в данной строке.


text = input("Введите строку:")
count = 0
sub_str = set("ауоыиэяюеё")
for index in text:
    if index not in sub_str:
        count += 1
print("Количество coгласных равно:")
print(count)
