# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
 def lucky_ticket(a, b, c, d, e, f):
    sum_left = a + b + c
    sum_right = d + e + f
    return sum_left == sum_right


if lucky_ticket(1, 3, 3, 4, 2, 1):
    print("lucky")
else:
    print("unlucky")



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
