# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_len_name = 0
name = ""

for list_name in names:
    if max_len_name < len(list_name):
        max_len_name = len(list_name)
        name = list_name
print(name)
