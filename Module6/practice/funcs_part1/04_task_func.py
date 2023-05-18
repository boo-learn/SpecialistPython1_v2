def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4)


def can_triangle(x1, y1, x2, y2, x3, y3) -> bool:
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    return a + b > c and a + c > b and b + c > a


# Пример вызова функции
print(can_triangle(10, 12, 14, 18, 12, 12))
print(can_triangle(0, 0, 5, 0, 0, -5))
print(can_triangle(-270, 0, 5, 0, 0, -5))

# Не забудьте протестировать вашу функцию
