# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_len_name = 0

for name in names:
    if len(name) > max_len_name:
        max_len_name = len(name)

for name in names:
    if len(name) == max_len_name:
        print(name)
        break
