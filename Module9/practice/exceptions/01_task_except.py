# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.
while True:
    try:
        string = input(" Ввести строку nxm: ")
        n, m = string .split('x')
        n, m = int(n), int(m)
        break
    except ValueError:
        print("ошибка формата, ввести сроку nxm")

if n < m:
    n, m = m, n

count = 0
while n >= m:
    count += n // m
    n = n % m

print(f"{count} квадратов получится отрезать со стороны {m}")
