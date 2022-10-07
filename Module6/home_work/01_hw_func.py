# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def sum_of_number(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total


def lucky_ticket(ticket_number):
    return sum_of_number(ticket_number // 1000) == sum_of_number(ticket_number % 1000)

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
