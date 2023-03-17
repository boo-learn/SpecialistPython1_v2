# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) < 6 or len(str(ticket_number)) > 6:
        return("В билете не 6 цифр, он не счастливый -(")
    else:
        a_1 = ticket_number // 100000
        a_2 = ticket_number % 100000 // 10000
        a_3 = ticket_number % 10000 // 1000
        a_4 = ticket_number % 1000 // 100
        a_5 = ticket_number % 100 // 10
        a_6 = ticket_number % 10
        if a_1 + a_2 + a_3 == a_4 + a_5 + a_6:
            return ("Билет счастливый")
        else:
            return("Билет не счастливый")


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
