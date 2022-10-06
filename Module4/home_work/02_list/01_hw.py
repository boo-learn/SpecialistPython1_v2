# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

for name in names:
    print(name, end="")
    if name != names[len(names) - 1]:
        print(", ", end="")

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
