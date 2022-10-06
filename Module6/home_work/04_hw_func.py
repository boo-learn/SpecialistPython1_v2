# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
def gcd_fun(x, y):
    if (y == 0):
        return x
    else:
        return gcd_fun(y, x % y)


def fraction(expression):
    list_expression = expression.split()
    list_expression_1 = list_expression[0].split('/')
    list_expression_2 = list_expression[2].split('/')
    if len(list_expression_1) == 1:
        list_expression_1 = [list_expression_1, '1']
    if len(list_expression_2) == 1:
        list_expression_2 = [list_expression_2[0], '1']
    expression_1 = [0, 0]
    expression_2 = [0, 0]
    expression_res = [0, 0]
    for i in range(2):
        expression_1[i] = int(list_expression_1[i])
        expression_2[i] = int(list_expression_2[i])

    if list_expression[1] == '+':
        expression_res[0] = expression_1[0] * expression_2[1] + expression_2[0] * expression_1[1]
    else:
        expression_res[0] = expression_1[0] * expression_2[1] - expression_2[0] * expression_1[1]

    expression_res[1] = expression_2[1] * expression_1[1]
    hole = expression_res[0] // expression_res[1]
    numerator = (expression_res[0] % expression_res[1])
    denominator = expression_res[1]
    gcd = gcd_fun(numerator, denominator)

    hole = hole if hole != 0 else ''
    numerator /= gcd
    denominator /= gcd
    res = f'{hole} {numerator:.0f}/{denominator:.0f} '
    res = res if numerator != 0 else 0
    return res


print(fraction(input('введи дробь: ')))

