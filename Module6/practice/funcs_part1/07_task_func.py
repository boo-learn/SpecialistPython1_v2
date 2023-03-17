# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def sec_to_time(s):
    hours = s // 3600
    tail = s % 3600
    minutes = tail // 60
    seconds = tail % 60
    return (f"{hours:02d}:{minutes:02d}:{seconds:02d}")



print(sec_to_time(29143))
