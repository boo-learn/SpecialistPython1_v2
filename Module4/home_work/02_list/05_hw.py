# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

max_name = ""
for name in names:
    if len(name) > len(max_name):
        max_name = name

print(max_name)
