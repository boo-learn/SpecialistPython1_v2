# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def time_in_format(seconds):
    hour = seconds // 3600 % 24
    minute = seconds % 3600 // 60
    secs = seconds % 60
    hour = hour if hour > 9 else "0"+str(hour)
    minute = minute if minute > 9 else "0" + str(minute)
    secs = secs if secs > 9 else "0" + str(secs)
    return (f"{hour}:{minute}:{secs}")


print(time_in_format(29143))
