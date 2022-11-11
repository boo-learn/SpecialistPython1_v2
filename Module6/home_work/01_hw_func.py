# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
   lucky = [int(count) for count in str(ticket_number)]
    if 7 > len(lucky) > 5:
        if sum(lucky[:3])==sum(lucky[3:]):
            return True
    else:
        return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
