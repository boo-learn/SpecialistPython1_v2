# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

max_length = 0
longest_name = ''

for name in names:
    if len(name) > max_length:
        max_length = len(name)
        longest_name = name

print(longest_name)
