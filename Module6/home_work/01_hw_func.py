# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if ticket_number < 100000:
        return False
    sum1 = 0
    sum2 = 0
    for i, n in enumerate(str(ticket_number)):
        if i < 3:
            sum1 += int(n)
        else:
            sum2 += int(n)
    return sum1 == sum2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(10001))
print(lucky_ticket(436751))
