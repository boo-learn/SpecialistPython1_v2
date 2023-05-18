# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number) -> bool:
    line = str(ticket_number)
    if len(line) != 6:
        return False
    return int(line[0]) + int(line[1]) + int(line[2]) == int(line[3]) + int(line[4]) + int(line[5])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(100011))
print(lucky_ticket(123456))
