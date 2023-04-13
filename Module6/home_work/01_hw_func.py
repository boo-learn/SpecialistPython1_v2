# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def str_sum(s):
    i = 0
    total = 0
    while i < len(s):
        total += int(s[i])
        i += 1
    return total


def lucky_ticket(ticket_number):
    t = str(ticket_number)
    if len(t) == 6:
        return str_sum(t[:3]) == str_sum(t[3:])
    else:
        return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(936751))
print(lucky_ticket(135351))
