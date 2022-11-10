# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_numbers = list(map(int, str(ticket_number)))
    if len(ticket_numbers) >= 6:
        if ticket_numbers[0] + ticket_numbers[1] + ticket_numbers[2] == \
                ticket_numbers[-1] + ticket_numbers[-2] + ticket_numbers[-3]:
            message = "Счастливый билетик! :)"
        else:
            message = "Билетик несчастливый :("
    else:
        message = "В билете недостаточно цифр"
    return message


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(156733))
print(lucky_ticket(414))
