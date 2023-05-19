# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

s = input("Введите стороны прямоугольника: ")
lst = []
def numbers(s):
    mum = 0
    first_arg = s[0:s.find('x')]
    second_arg = s[s.find('x')+1:]
    lst.append(first_arg)
    lst.append(second_arg)
    for i in lst:
        try:
            num = int(lst[0])//int(lst[1])
        except ValueError:
            return "Введен неверный формат"
    return num


res = numbers(s)
print(res)
