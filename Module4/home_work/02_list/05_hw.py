# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
max_lenght = 0
for name in names:
    if len(name) > max_lenght:
        max_lenght = len(name)
        max_name = name
print(max_name)
