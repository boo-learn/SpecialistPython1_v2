# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def sec_to_time(a):
    hours = a // 3600
    minuts = (a - hours * 3600) // 60
    seconds = a - hours * 3600 - minuts * 60
    return f"{hours:02d}:{minuts:02d}:{seconds:02d}"
