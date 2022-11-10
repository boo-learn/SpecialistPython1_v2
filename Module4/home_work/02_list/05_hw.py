# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр", "Александр II"]
best_name = ""
for name in names:
    if len(name) > len(best_name):
        best_name = name
print("Самое лучшее имя:", best_name)

# TODO: your code here
