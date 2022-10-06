# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_len = 0
for name in names:
    if max_len < len(name):
        maxlen_name = name
        max_len = len(name)
print(maxlen_name)

