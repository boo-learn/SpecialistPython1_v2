# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
summ_name = ""

for name in names:
    summ_name += name + ", "

print(summ_name.rstrip(", "))

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
