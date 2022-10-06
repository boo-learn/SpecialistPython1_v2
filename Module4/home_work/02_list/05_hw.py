# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# Вариант1
max_len = 0
for name in names:
    if len(name) > max_len:
        max_len = len(name)

for name in names:
    if len(name) == max_len:
        print(name)
        break

# Вариант2
max_name = ""
for name in names:
    if len(name) > len(max_name):
        max_name = name

print(max_name)

