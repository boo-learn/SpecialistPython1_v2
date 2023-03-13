# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    sum_p1, sum_p2 = 0, 0
    for p1 in (str(ticket_number)[:3]):
        sum_p1 += int(p1)
    for p2 in (str(ticket_number)[3:]):
        sum_p2 += int(p2)
    if len(str(ticket_number)) != 6:
        return "Некорректно введенный номер"
    elif sum_p1 == sum_p2:
        return "Счастливый билет!"
    else:
        return "Обычный билет"


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(123456))
