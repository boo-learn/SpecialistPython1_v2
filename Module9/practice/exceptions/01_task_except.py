# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

try:
    n = input("Введите размер прямоугольника: ")
    amout = int(n[0]) // int(n[2])
    print(amout)
except ValueError:
    print("Введены некорректные значения")
except IndexError:
    print("Введите размер прямоугольника как axb")
