# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


def lucky(x):
    return x // 100000 + x // 10000 % 10 == x % 100 // 10 + x % 10


print(lucky(115511))
print(lucky(124321))
print(lucky(436751))
