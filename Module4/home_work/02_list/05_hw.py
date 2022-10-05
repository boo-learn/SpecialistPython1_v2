# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
names.sort(key=len, reverse=True)
print(names[0])
print(max(names, key=len))

# TODO: your code here
