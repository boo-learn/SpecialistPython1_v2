# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них



names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_len = len(names[0])
max_len_name = []
for name in names:
    if len(name) >= max_len:
        max_len = len(name)
        max_len_name.append(name)

print("Самое длинное имя: ", max_len_name.pop())
