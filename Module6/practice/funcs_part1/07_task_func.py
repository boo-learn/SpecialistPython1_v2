# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def get_formatted_time(s: int) -> str:
    hours = s % 86400 // 3600
    minutes = s % 86400 % 3600 // 60
    seconds = s % 60
    return f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}"


seconds = int(input("Прошло секунд всего: "))
print(get_formatted_time(seconds))
