# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

rectangle = input("nxm:")

try:
    if rectangle.find("x") == -1:
        raise ValueError("value error")
    else:
        sides = rectangle.split("x")
        print(int(sides[0]) // int(sides[1]))
except ValueError as e:
    print(e)
