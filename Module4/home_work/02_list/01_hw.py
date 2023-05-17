# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
line = ""

for name in names:
    line = f"{line} {name},"
line = line[:-1]

print(line)
