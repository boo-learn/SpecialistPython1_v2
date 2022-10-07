# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    ticket_str_rev = ticket_str[::-1]
    if len(ticket_str) != 6:
        return False
    else:
        summ1 = 0
        summ2 = 0
        for i in range(0, 3):
            summ1 += int(ticket_str[i])
            summ2 += int(ticket_str_rev[i])
        if summ1 == summ2:
            return True
        else:
            return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(433281))
