# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    t_number = str(ticket_number)
    if len(t_number) == 6:
        sum1 = int(t_number[0])+int(t_number[1])+int(t_number[2])
        sum2 = int(t_number[3]) + int(t_number[4]) + int(t_number[5])
        return sum1 == sum2
    else:
        return


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
