# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

first = True
for name in names:
    if first:
        first = False
    else:
        print(",", end=" ")
    print(name, end="")

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
