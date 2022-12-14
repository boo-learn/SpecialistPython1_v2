# Открываем файл на чтение. "r" - read(чтение)
# encoding - кодировка файла
# files - имя директории(данная директория должна находиться в той же директории, что и текущий файл)
# data.txt - имя файла
f = open("files/data.txt", "r", encoding="UTF-8")

# Через переменную f выполняем операции с файлом
# .readline() - считывает одну строку из файла
line = f.readline()
print("first line in file:", line)

# По файлу можно итерировать, считывая строку за строкой, пока файл не закончится
# Перед выводом строку(line) оборачиваем в функцию repr() чтобы увидеть нечитаемые символы. Видим наличия /n в строке
print("Выводим содержимое файла без первой строки, т.к. первую строку мы считали ранее методом readline():")
for line in f:
    print("next line:", repr(line))

# Перемещаем указатель на чтение в начало файла, чтобы снова прочитать содержимое файла
f.seek(0)

# Повторно читаем файл построчно. Метод rstrip() удаляет пробельные символы справа у строки.
print("\nВыводим содержимое файла, удалив символы переноса строки:")
for line in f:
    print("next line:", line.rstrip())

# По окончании работы с файлом - закрываем его.
f.close()
