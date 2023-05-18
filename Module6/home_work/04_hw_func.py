# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def get_fraction(s: str) -> dict:
    integer_part = 0
    numerator = 0
    denominator = 1
    parts = s.strip().split(" ")
    fraction_part = parts[0]
    if fraction_part.find("/") == -1:
        integer_part = int(fraction_part)
        if len(parts) > 1:
            fraction_part = parts[1]
        else:
            fraction_part = ""
    if fraction_part.find("/") != -1:
        numerator = int(fraction_part.split("/")[0])
        denominator = int(fraction_part.split("/")[1])
    return dict(integer_part=integer_part, numerator=numerator, denominator=denominator)


def fract_addition(f1: dict, f2: dict) -> dict:
    result = dict(integer_part=f1["integer_part"] + f2["integer_part"], numerator=0, denominator=1)
    i = 2
    while i < f1["denominator"] * f2["denominator"]:
        if f1["denominator"] % i == 0 and f2["denominator"] % i == 0:
            break;
        i += 1
    result["denominator"] = i
    f1["numerator"] *= int(result["denominator"] / f1["denominator"])
    f2["numerator"] *= int(result["denominator"] / f2["denominator"])
    result["numerator"] = f1["numerator"] + f2["numerator"]
    result["integer_part"] += result["numerator"] // result["denominator"]
    result["numerator"] = result["numerator"] % result["denominator"]
    return result


def fract_subtraction(f1: dict, f2: dict) -> dict:
    result = dict(integer_part=f1["integer_part"] - f2["integer_part"], numerator=0, denominator=1)
    i = 2
    while i < f1["denominator"] * f2["denominator"]:
        if f1["denominator"] % i == 0 and f2["denominator"] % i == 0:
            break;
        i += 1
    result["denominator"] = i
    f1["numerator"] *= int(result["denominator"] / f1["denominator"])
    f2["numerator"] *= int(result["denominator"] / f2["denominator"])
    result["numerator"] = f1["numerator"] - f2["numerator"]
    result["integer_part"] += result["numerator"] // result["denominator"]
    result["numerator"] = result["numerator"] % result["denominator"]
    return result


def math_operation(s: str) -> dict:
    result = dict(integer_part=0, numerator=0, denominator=1)
    parts_addition = s.split("+")
    for part1 in parts_addition:
        parts_subtraction = part1.split("-")
        if len(parts_subtraction) > 1:
            first = True
            prev_part = "*"
            for part2 in parts_subtraction:
                if part2.strip() != "":
                    if first:
                        result = fract_addition(result, get_fraction(part2 if prev_part != "" else "-" + part2))
                        first = False
                    else:
                        result = fract_subtraction(result, get_fraction(part2 if prev_part != "" else "-" + part2))
                prev_part = part2.strip()
        else:
            result = fract_addition(result, get_fraction(part1))
    return result


def calc_fraction(s: str) -> str:
    result = math_operation(s)
    return f"{result['integer_part']} {result['numerator']}/{result['denominator']}"


print(calc_fraction("5/6 + 4/7"))
print(calc_fraction("-2/3 - -2"))

