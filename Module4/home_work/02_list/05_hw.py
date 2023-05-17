# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

#Вариант 1
max_length = 0
max_name = ""
for name in names:
    if len(name) > max_length:
        max_name = name
        max_length = len(name)

print(max_name)

#Вариант 2
names.sort(key=lambda x: len(x), reverse=True)
print(names[0])
