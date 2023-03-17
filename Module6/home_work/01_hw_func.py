# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    string = str(ticket_number)
    if len(string) == 6:
        left_sum = int(string[0]) + int(string[1]) + int(string[2])
        right_sum = int(string[-1]) + int(string[-2]) + int(string[-3])
        return left_sum == right_sum
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
