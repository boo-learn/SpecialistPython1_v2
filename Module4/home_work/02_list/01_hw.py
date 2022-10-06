# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]


# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

# Вариант1
string = ""
for name in names:
    string += name + ", "
string = string[:-2]
print(string)

# Вариант2
string2=", ".join(names)
print(string2)

# Вариант3
print(*names, sep=", ")
