# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

count = 0
length = 0
i = 0
string = ""
for a in names:
    if length < len(a):
        length = len(a)
        count = i
    i += 1
    
print(names[count])
