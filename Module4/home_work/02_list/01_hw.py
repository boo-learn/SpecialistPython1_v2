# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
str_names = ""
index = 0

while index < len(names):
    str_names += names[index]
    index += 1
    if index < len(names):
        str_names += ", "

print(str_names)

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
