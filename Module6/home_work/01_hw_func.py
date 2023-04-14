# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def is_lucky(ticket_number):

    ticket_str = str(ticket_number)

    if len(ticket_str) != 6:
        return "Введите число из 6 цифр"#False
        
    first_half_sum = sum(map(int, ticket_str[:3]))
    second_half_sum = sum(map(int, ticket_str[3:]))

    if first_half_sum == second_half_sum:
        return "Билет счастливый"#True
    else:
        return "Билет несчастливый"#False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
