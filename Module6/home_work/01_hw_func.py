# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    list_number = [int(number) for number in str(ticket_number)]
    if len(list_number) == 6:
        if sum(list_number[:3]) == sum(list_number[3:]):
            return True
    return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
