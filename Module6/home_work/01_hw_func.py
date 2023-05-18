# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    long_ticket_number = len(str(ticket_number))
    count = 0
    summ1 = 0
    summ2 = 0
    for number in str(ticket_number):
        if count < long_ticket_number // 2:
            summ1 += int(number)
            count += 1
        elif long_ticket_number % 2 != 0 and count == long_ticket_number // 2:
            count += 1
        else:
            summ2 += int(number)
            count += 1
    result = f"{ticket_number} - Билет счастливый" if summ1 == summ2 else f"{ticket_number} - Билет не счастливый"
    return  result
    # Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(437751))
print(lucky_ticket(12345))
