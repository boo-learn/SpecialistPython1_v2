# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def plus_minus(a):
    divide = a.split()
    if divide[0].count('/'):
        first = divide[0].split('/')
    else:
        first = [int(divide[0]) * int(divide[0]), int(divide[0])]
    if divide[2].count('/'):
        second = divide[2].split('/')
    else:
        second = [int(divide[2]) * int(divide[2]), int(divide[2])]
    if divide[1] == '+':
        num = int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])
    else:
        num = int(first[0]) * int(second[1]) - int(first[1]) * int(second[0])
    den = int(second[1]) * int(first[1])

    if den < 0:
        den *= -1
        num *= -1
    hcf = 1
    for i in range(1, den):
        if (num % den) % i == 0 and den % i == 0:
            hcf = i
    return f'{num // den} {int((num % den) / hcf)}/{int(den / hcf)}'


text = '5/6 + 4/7'
print(plus_minus(text))


