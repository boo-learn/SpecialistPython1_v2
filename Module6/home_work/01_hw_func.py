# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    i = 1
    first_part = 0
    second_part = 0
    for number in ticket_number_str:
        if i < 4:
            first_part += int(number)
        else:
            second_part += int(number)
        i += 1
    return first_part == second_part


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
