# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    digits = []

    while ticket_number != 0:
        digits.append(ticket_number % 10)
        ticket_number = ticket_number // 10
    print(digits)

    if len(digits) % 2 != 0:
        return False

    sum1 = 0
    for digit in digits[:len(digits)//2]:
        sum1 += digit

    sum2 = 0
    for digit in digits[len(digits)//2:]:
        sum2 += digit

    if sum1 == sum2:
        return True
    else:
        return False



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
