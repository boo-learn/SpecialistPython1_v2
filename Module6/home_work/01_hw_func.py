# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    tickets = str(ticket_number)
    p1 = [*tickets[0:3]]
    p2 = [*tickets[3:]]
    summa1 = 0
    summa2 = 0
    for __ in p1:
        summa1 += int(__)
    for __ in p2:
        summa2 += int(__)
    if len(p2) != 3:
        print("Число не шестизначное")
    elif summa1 == summa2:
        print("Билет счастливый")
    else:
        print("Билет несчастливый")


lucky_ticket(123006)
lucky_ticket(12321)
lucky_ticket(436751)


