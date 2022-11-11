# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    return lambda x: (lambda x: 'True' if sum(x[:3]) == sum(x[3:]) else 'False')(list(map(int, list(str(x)))))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
