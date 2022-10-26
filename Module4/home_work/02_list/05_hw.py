# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
Characters = len(names[0])
for name in names:
    if len(name) > Characters:
        Characters = len(name)
        long_name = name
print(long_name)
