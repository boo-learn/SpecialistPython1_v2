# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
maximum_i = 0
maximum = 0
for name in names:
    if len(name) > maximum:
        maximum = len(name)
        maximum_i = names.index(name)
print(names[maximum_i])
