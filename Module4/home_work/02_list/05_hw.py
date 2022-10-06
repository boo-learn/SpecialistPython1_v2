# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_name = 0
for name in names:
    if len(name) > max_name:
        max_name = len(name)

for name in names:
    if len(name) == max_name:
        print(name)
