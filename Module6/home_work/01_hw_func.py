# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    start = ticket_number // 1000
    end = ticket_number % 1000
    start_sum = start // 100 + start // 10 % 10 + start % 10
    end_sum = end // 100 + end // 10 % 10 + end % 10
    
    if start_sum == end_sum:
        return "Счастливый билет"
    else:
        return "Несчастливый билет"
    
# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
