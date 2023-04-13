# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        digit_1 = int(str(ticket_number)[0])
        digit_2 = int(str(ticket_number)[1])
        last_digit = int(str(ticket_number)[-1])
        pre_last_digit = int(str(ticket_number)[-2])

        if digit_1 + digit_2 == pre_last_digit + last_digit:
            result = "Счастливый билет !"
        else:
            result = "Несчастный  билет !"
    else:
        result = "Должно быть 6 цифр !"
    return result


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
