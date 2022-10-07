# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
while True:
    data = input("Введите данные: ")
    try:
        line = data.split('x')
        print(f'Данные корректны, квадратов {int(line[0]) // int(line[1])}')
        break
    except:
        print('Введены некорректные данные')
