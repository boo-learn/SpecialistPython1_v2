# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number: int) -> bool:

    sum_numbers_part1 = 0
    sum_numbers_part2 = 0
    count_check_num = 0

    for number in str(ticket_number):
        count_check_num += 1
        if count_check_num <= 3:
            sum_numbers_part1 += int(number)
        else:
            sum_numbers_part2 += int(number)

    return sum_numbers_part1 == sum_numbers_part2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321)) # дано, что билет имеет 6 знаков. 
print(lucky_ticket(436751))
