# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

#names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
import random
#           4       5           8           7       4       8
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр", "Афанасий"]
new_names = []
letters = 0

for single_name in names:
    if len(single_name) > letters:
        letters = len(single_name)
        new_names.clear()
        new_names.append(single_name)
    elif len(single_name) == letters:
        new_names.append(single_name)

print(random.choice(new_names))

# TODO: your code here
