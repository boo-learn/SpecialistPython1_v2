# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def to_integer_part(numerator, denominator):
    return numerator // denominator, numerator % denominator, denominator


def to_fractional(integer_part, numerator, denominator):
    if denominator:
        return integer_part * denominator + numerator * (1 if integer_part >= 0 else -1), denominator
    else:
        return integer_part, 1


def sum_fractional_numbers(number1, number2, operation='+'):
    if operation == '+':
        return number2[1] * number1[0] + number1[1] * number2[0], number1[1] * number2[1]
    else:
        return number2[1] * number1[0] - number1[1] * number2[0], number1[1] * number2[1]

def string_decomposition(string):
    parts_of_example = string.split()
    operation = ''
    numbers = [[0, 0, 0], [0, 0, 0]]
    number = 0
    for el in parts_of_example:
        if el.find('/') != -1:
            numerator, denominator = el.split('/')
            numbers[number][1] = int(numerator)
            numbers[number][2] = int(denominator)
        elif el == '-' or el == '+':
            operation = el
            number += 1
        else:
            numbers[number][0] = int(el)
    return numbers, operation


string = input("string: ")

numbers, operation = string_decomposition(string)
answer = to_integer_part(
    *sum_fractional_numbers(to_fractional(*numbers[0]), to_fractional(*numbers[1]), operation=operation))
if answer[1]:
    if answer[0]:
        print(f"{string} = {answer[0]} {answer[1]}/{answer[2]}")
    else:
        print(f"{string} = {answer[1]}/{answer[2]}")
else:
    print(f"{string} = {answer[0]}")


