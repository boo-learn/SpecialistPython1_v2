# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

from random import randrange
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

name_max_len = len(max(names, key=len))
longest_names = []

for name in names:
    if len(name) == name_max_len:
        longest_names.append(name)

if len(longest_names) > 1:
    print(longest_names[randrange(len(longest_names))])
else:
    print(*longest_names)
