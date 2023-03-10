# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
# list_names = str(names)
# format_str = list_names.replace("'", "")
# format_str1 = format_str.replace("]", "")
# format_str2 =  format_str1.replace("[", "")
# print(format_str2)
print(*names, sep=", ")
