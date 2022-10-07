# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    str_tick = str(ticket_number)
    l = len(str_tick)
    sum1 = 0
    sum2 = 0
    for el in str_tick[:(l // 2)]:
        sum1 += int(el)
    for el in str_tick[-(l // 2):]:
        sum2 += int(el)
    return sum2 == sum1


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(4367500))
