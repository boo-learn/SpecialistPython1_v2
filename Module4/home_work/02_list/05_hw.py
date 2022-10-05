# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

num_symb = 0
for name in names:
    if len(name) > num_symb:
        longest = name
        num_symb = len(name)
print(longest)
