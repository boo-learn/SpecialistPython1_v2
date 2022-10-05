names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
large_name = ""
size = 0
for name in names:
    if len(name) > size:
        large_name = name
        size = len(name)
print(large_name)
print(size)

