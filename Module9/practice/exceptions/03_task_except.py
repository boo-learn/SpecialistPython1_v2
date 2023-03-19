# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.


input_str = "2 12 -45 7 10"
try:
    numbers = list(map(int, input_str.split()))
    if len(numbers) != 5:
        raise ValueError('Входная строка должна содержать ровно 5 чисел')

    min_positive = None
    for number in numbers:
        if number > 0 and (min_positive is None or number < min_positive):
            min_positive = number

    if min_positive is None:
        print('Нет положительных чисел во входных данных')
    else:
        print(min_positive)

except ValueError as e:
    print(f'Ошибка: {e}')
except Exception as e:
    print(f'Неожиданная ошибка: {e}')
