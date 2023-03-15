# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
leng = 0
final = ""

for name in names:
    if leng < len(name):
        leng = len(name)
        final = name
        
print(final)
