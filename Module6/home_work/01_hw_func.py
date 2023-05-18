# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) % 2 != 0:
        return False
    left = map(int, ticket_str[:len(ticket_str) // 2])
    right = map(int, ticket_str[len(ticket_str) // 2:])
    return sum(left) == sum(right)

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
