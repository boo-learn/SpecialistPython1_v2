# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
while True:
    try:
        ex = input("nxm: ")

        numbers = ex.split("x")
        n = int(numbers[0])
        m = int(numbers[1])
        break
    except ValueError:
        print("Неверный формат выражения")
    except IndexError:
        print("Неверный формат выражения")
try:
    if n > m:
        print(n // m)
    else:
        print(m // n)
except ZeroDivisionError:
    print('Делить на ноль нельзя')
