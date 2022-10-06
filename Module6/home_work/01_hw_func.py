# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
def lucky_ticket(ticket_number):
    num_list = []
    for num in str(ticket_number):
        num_list.append(num)
    f_sum = 0
    r_sum = 0
    for num1 in num_list[0:3]:
        f_sum += int(num1)
    for num2 in num_list[3:6]:
        r_sum += int(num2)
    return f_sum == r_sum
# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
