# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_length = 0
i = 0
while i < len(names):
    if max_length < len(names[i]):
        max_length = len(names[i])
        max_length_index = i
    i += 1
print(names[max_length_index])
