# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    digits = str(ticket_number)
    i = 0
    sum_first = 0
    sum_second = 0
    n = len(digits) // 2
    while i < n:
        sum_first += int(digits[i])
        sum_second += int(digits[len(digits) - i -1])
        i += 1
    return sum_first == sum_second


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
