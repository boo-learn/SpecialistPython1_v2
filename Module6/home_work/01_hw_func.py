# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number: int):
    """
    :param num: число для проверки
    :return: число счастливое/число не является счастливым
    """
    first_part = str(ticket_number // 1000)
    last_part = str(ticket_number % 1000)
    first_part_sum = 0
    last_part_sum = 0

    for num_f in first_part:
        first_part_sum += int(num_f)

    for num_l in last_part:
        last_part_sum += int(num_l)

    if first_part_sum == last_part_sum:
        return "Счастливое число"
    return "Число не является счастливым"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
