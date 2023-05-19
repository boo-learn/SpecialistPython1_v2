# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.

row = input("row: ")

numbers = row.split(" ")
min_positive_number = -1
first = True
try:
    for number in numbers:
        n = int(number)
        if n > 0:
            if first:
                min_positive_number = n
                first = False
            elif n < min_positive_number:
                min_positive_number = n

except:
    print("данные в неверном формате")

if min_positive_number != -1:
    print("min_positive_number: ", min_positive_number)
else:
    print("positive_number not found")
