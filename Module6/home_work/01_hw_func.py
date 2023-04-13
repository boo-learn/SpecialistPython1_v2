# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)  # преобразуем билет в строку
    half_len = len(ticket_str) // 2  # делим и округляем
    first_half = ticket_str[:half_len]  # первая половина
    second_half = ticket_str[half_len:]  # вторая половина
    sum_first_half = sum(int(x) for x in first_half)  # сумма первой половины
    sum_second_half = sum(int(x) for x in second_half)  # сумма второй половины
    if sum_first_half == sum_second_half:
        print(f"Билет {ticket_number} не является счастливым.")
    else:
        print(f"Билет {ticket_number} является счастливым! ")


# Тестируем функцию
lucky_ticket(123006)  # Билет 123006 не является счастливым.
lucky_ticket(12321)  # Билет 12321 является счастливым!
lucky_ticket(436751)  # Билет 436751 является счастливым!


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
