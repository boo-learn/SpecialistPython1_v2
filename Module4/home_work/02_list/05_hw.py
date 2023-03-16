# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_length = 0
max_length_word = ""

for element in names:
    if len(element) > max_length:
        max_length = len(element)
        max_length_word = element

print(max_length_word)


# TODO: your code here
