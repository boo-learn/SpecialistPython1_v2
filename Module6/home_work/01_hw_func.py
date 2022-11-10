# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return "номер билета должен состоять из 6 цифр"
    else:
        num_list = list(str(ticket_number))
        sum_first_half = 0
        sum_second_half = 0
        for num in num_list[:3]:
            sum_first_half += int(num)
        for num in num_list[3:]:
            sum_second_half += int(num)
        if sum_first_half == sum_second_half:
            return True
        else:
            return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
