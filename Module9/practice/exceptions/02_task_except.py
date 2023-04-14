# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.

def is_leap_year(year):
   
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    
    if month < 1 or month > 12:
        return "Ошибка: введите корректный номер месяца"
    
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return days_in_month[month - 1]


while True:
    try:
        month, year = input("введите месяц год (MM YYYY): ").split()
        month = int(month)
        year = int(year)
        break
    except ValueError:
        print("некорректно введены данные")


days = days_in_month(month, year)

if isinstance(days, str):
    print(days)
else:
    print( days, "дней в", month, year)

