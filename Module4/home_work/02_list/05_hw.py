# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_len = 0

for name in names:
    if max_len < len(name):
        max_len = len(name)
        max_name = name

print(max_name)

