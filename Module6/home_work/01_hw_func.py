# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    string = str(ticket_number)
    firsts = 0
    lasts = 0

    if len(string) != 6:
        return "число не 6 значное!"

    for elem in range(int(len(string) / 2)):
        firsts += int(string[elem])
        lasts += int(string[-1 - elem])

    if firsts == lasts:
        return "Число счастливое!"
    else:
        return "Определенно нет!"


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
