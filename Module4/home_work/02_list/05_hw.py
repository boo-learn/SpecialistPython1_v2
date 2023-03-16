# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here


names = ["Иван", "Ирина", "Вячеслав", "ВасилийВторой", "Петр", "Василий"]

i = 0
max_len = len(names[i])
max_len_name = names[i]
for name in names:
    if len(name) > max_len:
        max_len = len(names[i])
        max_len_name = names[i]
    i += 1
print(max_len_name)
print(max_len)
