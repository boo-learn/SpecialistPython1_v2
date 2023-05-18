# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    str_number = str(ticket_number)
    start_number1 = str_number[0]
    start_number2 = str_number[1]
    end_number1 = str_number[-1]
    end_number2 = str_number[-2]
    return start_number1 + start_number2 == end_number1 + end_number2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
