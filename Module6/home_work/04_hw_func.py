# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

fraction = input('Введите условие:')
first_number = fraction[0:fraction.find(' ')]
second_number = fraction[:fraction.find(' ') + 2:-1][::-1]
sign = fraction[fraction.find(' '): -1][1]
if first_number.find('/') != -1:
    frst_denominator = first_number[first_number.find('/') + 1:]
    frst_numerator = first_number[:first_number.find('/')]
    if second_number.find('/') != -1:
        scnd_denominator = second_number[second_number.find('/') + 1:]
        scnd_numerator = second_number[:second_number.find('/')]
        if frst_denominator != scnd_denominator:
            common_denominator = int(frst_denominator) * int(scnd_denominator)
            numerator = int(frst_numerator) * int(scnd_denominator) + int(scnd_numerator) * int(frst_denominator)
            whole = numerator // common_denominator
            print(str(whole), " ", numerator % common_denominator, "/", common_denominator, sep='')
        elif frst_denominator == scnd_denominator:
            common_denominator = int(frst_denominator)
            numerator = int(frst_numerator) + int(scnd_numerator)
            whole = numerator // common_denominator
            print(str(whole), " ", numerator % common_denominator, "/", common_denominator, sep='')
    elif second_number.find('/') == -1:
        scnd_denominator = int(frst_denominator)
        scnd_numerator = int(second_number) * int(frst_denominator)
        common_denominator = int(frst_denominator)
        numerator = int(frst_numerator) + int(scnd_numerator)
        whole = numerator // common_denominator
        print(str(whole), " ", numerator % common_denominator, "/", common_denominator, sep='')
elif first_number.find('/') == -1:
    if second_number.find('/') != -1:
        scnd_denominator = second_number[second_number.find('/') + 1:]
        scnd_numerator = second_number[:second_number.find('/')]
        frst_denominator = int(scnd_denominator)
        frst_numerator = int(first_number) * int(scnd_denominator)
        common_denominator = int(scnd_denominator)
        numerator = int(frst_numerator) + int(scnd_numerator)
        whole = numerator // common_denominator
        print(str(whole), " ", numerator % common_denominator, "/", common_denominator, sep='')
    else:
        print(int(first_number) + int(second_number))


