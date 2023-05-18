# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    number = []
    for i in str(ticket_number):
        number.append(i)
    left_sum_num = int(number[0]) + int(number[1]) + int(number[2])
    right_sum_num = int(number[3]) + int(number[4]) + int(number[5])
    if left_sum_num == right_sum_num:
        return True
    return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
