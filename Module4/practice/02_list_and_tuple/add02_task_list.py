# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь
current_date = input("current_date : ")
current_date_list = current_date.split(".")
current_date_int = int(current_date_list[0])
# print(current_date_int)
current_month_int = int(current_date_list[1])
# print(current_month_int)
current_year_int = int(current_date_list[2])
# print(current_year_int)
days_list = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое"]
month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
              "декабрь"]
print(f"{days_list[current_date_int - 1]} {month_list[current_month_int - 1]} {current_year_int} года")
