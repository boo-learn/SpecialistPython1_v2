# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    s = str(ticket_number)
    if int(s[0]) + int(s[1]) + int(s[2]) == int(s[-1]) + int(s[-2]) + int(s[-3]):
        return True
    else:
        return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
