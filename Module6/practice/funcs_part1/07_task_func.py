# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def time_format(sec):
    seconds = sec % 60
    minutes = sec % 3600 // 60
    hours = sec // 3600
    return f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}"


print(time_format(29143))
